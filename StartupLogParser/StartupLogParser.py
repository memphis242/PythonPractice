# For working with command-line arguments
import sys
import os
# For working with the .csv / Excel sheets:
import csv
import pandas as pd


# Constants for the whole file
OUTPUT_CSV_FILE_NAME = 'StartupLog.csv'
LOG_MSG_PGN_STRING = 'F389'   # 62345
LOG_MSG_TLA_STRING = 'DA'     # Diagnostic Tool?
LOG_MSG_CMD_BYTE_MSG1 = '00'
LOG_MSG_CMD_BYTE_MSG2 = '01'
LOG_MSG_CMD_BYTE_TIME_STAMP_MSG1 = '02'
LOG_MSG_CMD_BYTE_TIME_STAMP_MSG2 = '03'

# Print initial display message...
print('\nRunning StartupLogParser.py...')


#########################################################################
# Obtain input sheet from command-line arguments
#########################################################################
# Iterate through input arguments to find file specification
file_name = ''
if len( sys.argv[1:] ) <= 0:
   raise FileNotFoundError('No file specified!')

else:
    file_name = sys.argv[1]
#file_name = 'StartupLog_Test2.txt'

# Inform of input file...
print(f'Input file is: {file_name}')

# Determine validity of file...
if (file_name.find('.txt') == -1) and (file_name.find('.log') == -1):
    raise ValueError('Incorrect file type specified! Needs to be a .txt or .log file.')


#########################################################################
# Read input file that was specified and extract relevant data
#########################################################################
print('Parsing the log data...')
lines = []  # Will hold each line of the file
data_bytes_list = []
log_dictionary_list = []
log_dictionary_item = {}
timestamp = 0
startup_event_timestamps = { 'Left Inverter Address Claim Timestamp (ms)':0, 'Right Inverter Address Claim Timestamp (ms)':0, 'Left Inverter Invalid to Valid Timestamp (ms)':0, 'Right Inverter Invalid to Valid Timestamp (ms)':0 }

with open( file_name, 'r', newline='' ) as log_file:
   lines = log_file.readlines()

   row = 0    # Row of table I'll build up that will be output to a .csv file
   found_time_stamp_msg1 = False
   found_time_stamp_msg2 = False
   for line in lines:
      line = line.strip()  # Remove any leading/trailing whitespace
      line = line.split()  # Split the line by whitespace

      if line[0] != 'r':   # Only scan lines that start with 'r' to indicate a message line from a received message
         continue

      pgn = line[3][2:6]
      source_address = line[3][-2:]
      if line[3][2:6] == LOG_MSG_PGN_STRING and line[3][-2:] == LOG_MSG_TLA_STRING :    # If this line is our log message line...
         # Get the data bytes!
         data_bytes = line[5:13]
         data_bytes_list.append( data_bytes )

         # Based on the command byte, decide what data this is and place into log dictionary
         if data_bytes[0] == LOG_MSG_CMD_BYTE_MSG1:
            # Message 1 contains left motor speed, right motor speed, and left motor torque, each 2 bytes in length, taking up bytes 2 through 7 (1-indexed)
            left_motor_speed = ( int( data_bytes[2] + data_bytes[1], 16 ) * 0.5 ) - 16000
            right_motor_speed = ( int( data_bytes[4] + data_bytes[3], 16 ) * 0.5 ) - 16000
            left_motor_torque = ( ( int( data_bytes[6] + data_bytes[5], 16 ) * 0.00390625 ) - 125 ) * 7.65     # Converting the percentage torque reported to an absolute torque based on 765 Nm reference

            log_dictionary_item['Left Motor Speed'] = left_motor_speed
            log_dictionary_item['Right Motor Speed'] = right_motor_speed
            log_dictionary_item['Left Motor Torque'] = left_motor_torque


         elif data_bytes[0] == LOG_MSG_CMD_BYTE_MSG2:
            # Message 2 contains right motor torque, left motor speed estimate, and right motor speed estimate, each 2 bytes in length, taking up bytes 2 through 7 (1-indexed)
            right_motor_torque = ( ( int( data_bytes[2] + data_bytes[1], 16 ) * 0.00390625 ) - 125 ) * 7.65     # Converting the percentage torque reported to an absolute torque based on 765 Nm reference
            left_motor_speed_estimate = ( int( data_bytes[4] + data_bytes[3], 16 ) * 0.5 ) - 16000
            right_motor_speed_estimate = ( int( data_bytes[6] + data_bytes[5], 16 ) * 0.5 ) - 16000

            log_dictionary_item['Right Motor Torque'] = right_motor_torque
            log_dictionary_item['Left Motor Speed Estimate'] = left_motor_speed_estimate
            log_dictionary_item['Right Motor Speed Estimate'] = right_motor_speed_estimate

            if row > 0:
               timestamp = timestamp + 5.000
               log_dictionary_item['Time Stamp (ms)'] = timestamp

            log_dictionary_list.append( log_dictionary_item.copy() )

            row = row + 1

         elif data_bytes[0] == LOG_MSG_CMD_BYTE_TIME_STAMP_MSG1:
            if found_time_stamp_msg1 == False:
               found_time_stamp_msg1 = True
               # Startup message contains the startup time in bytes 2 and 3 (1-indexed)
               startup_time_microseconds = int( data_bytes[2] + data_bytes[1], 16)
               timestamp = startup_time_microseconds / 1000.0

               log_dictionary_item['Time Stamp (ms)'] = timestamp

               # Get other startup-related time stamps. For msg1, these will include left inverter address claim timestamp and right inverter lower two bytes of address claim timestamp
               startup_event_timestamps['Left Inverter Address Claim Timestamp (ms)'] = int( data_bytes[5] + data_bytes[4] + data_bytes[3], 16) / 1000.0
               startup_event_timestamps['Right Inverter Address Claim Timestamp (ms)'] = int( data_bytes[7] + data_bytes[6], 16)

            else:
               # Not supposed to get this message again... Don't raise an exception but just print to stdout to report this
               print( f'WARNING: Extra time stamp message 1 was found at timestamp: { line[15] }. Ignored.' )
         
         elif data_bytes[0] == LOG_MSG_CMD_BYTE_TIME_STAMP_MSG2:
            if found_time_stamp_msg2 == False:
               found_time_stamp_msg2 = True

               # Get other startup-related time stamps. For msg1, these will include right inverter address claim timestamp MSB, left and right inverter invalid to valid timestamps
               startup_event_timestamps['Right Inverter Address Claim Timestamp (ms)'] = ( startup_event_timestamps['Right Inverter Address Claim Timestamp (ms)'] + ( int( data_bytes[1], 16) << 16 ) ) / 1000.0
               startup_event_timestamps['Left Inverter Invalid to Valid Timestamp (ms)'] = int( data_bytes[4] + data_bytes[3] + data_bytes[2], 16) / 1000.0
               startup_event_timestamps['Right Inverter Invalid to Valid Timestamp (ms)'] = int( data_bytes[7] + data_bytes[6] + data_bytes[5], 16) / 1000.0

            else:
               # Not supposed to get this message again... Don't raise an exception but just print to stdout to report this
               print( f'WARNING: Extra time stamp message 2 was found at timestamp: { line[15] }. Ignored.' )


         else:
            # Not supposed to get a message like this... Don't raise an exception but just print to stdout to report this
            print( f'ERROR: Unknown 62345 message received at timestamp: { line[15] }' )


#########################################################################
# Output information to a csv file
#########################################################################
# Use the name of the input log file for the csv file
output_csv_file_name = file_name[0:-4] + '.csv'
print(f'Exporting to {output_csv_file_name} file...')
with open( output_csv_file_name, 'w', newline='' ) as output_csv_file:
   writer = csv.writer( output_csv_file )
   writer.writerow( ['Left Inverter Address Claim Timestamp (ms)', startup_event_timestamps['Left Inverter Address Claim Timestamp (ms)'] ] )
   writer.writerow( ['Right Inverter Address Claim Timestamp (ms)', startup_event_timestamps['Right Inverter Address Claim Timestamp (ms)'] ] )
   writer.writerow( ['Left Inverter Invalid to Valid Timestamp (ms)', startup_event_timestamps['Left Inverter Invalid to Valid Timestamp (ms)'] ] )
   writer.writerow( ['Left Inverter Invalid to Valid Timestamp (ms)', startup_event_timestamps['Right Inverter Invalid to Valid Timestamp (ms)'] ] )
   writer.writerow('')
   writer.writerow( [ 'Time Stamp (ms)', 'Left Motor Speed', 'Right Motor Speed', 'Left Motor Torque', 'Right Motor Torque', 'Left Motor Speed Estimate', 'Right Motor Speed Estimate' ] )

   for item in log_dictionary_list:
      row = [ item['Time Stamp (ms)'], item['Left Motor Speed'], item['Right Motor Speed'], item['Left Motor Torque'], item['Right Motor Torque'], item['Left Motor Speed Estimate'], item['Right Motor Speed Estimate'] ]
      writer.writerow( row )

print('Done! :D\n')