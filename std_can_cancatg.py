
import csv
from std_can import unique, \
                    StdCAN_HashTableEntry, StdCAN_MessageSignal, SignalType

# Print initial display message...

#########################################################################
# Read in CSV data
#########################################################################
print('\t\tObtaining data from csv file...')

input_csv_data = []     # This variable will hold the list of dictionaries, where each dictionary represents a row
msg_id_list = []  # This list will hold the message IDs in the sheet, which turns out to be convenient later on
msg_name_list = []
signal_name_list = []
can_var_name_list = []
msg_signal_dictionary = {}
# Read in data from csv file into local object
with open('StdCANSheet_Updated.csv', 'r', newline='') as csvfile:
    # This DictReader object below can then be iterated over like a list of dictionaries with the column headers as the keys
    csv_reader = csv.DictReader(csvfile)
    
    for row in csv_reader:
        input_csv_data.append(row)

# Get information from input data
first_signal_in_msg = True
for idx, row in enumerate(input_csv_data):

    if row['Message / Signal'] == 'M':

        msg_id_list.append(row['MessageID'])
        msg_name_list.append(row['MessageName / SignalName'])
        first_signal_in_msg = True

        # Check if next row is also a message row, in which case
        # append empty signal to this signal
        if input_csv_data[idx + 1]['Message / Signal'] == 'M':
            msg_signal_dictionary[msg_name_list[-1]] = [ StdCAN_MessageSignal('NA', 0, 0, 0) ]

    else:
        if first_signal_in_msg == True:
            # If this is the first signal in the message, need to create a new list to set to this location in the dictionary
            msg_signal_dictionary[msg_name_list[-1]] = []
            first_signal_in_msg = False
        signal_name_list.append( row['MessageName / SignalName'] )
        can_var_name_list.append( f'CAN_11Bit_{ signal_name_list[-1] }' )
        msg_signal_dictionary[msg_name_list[-1]].append( StdCAN_MessageSignal( row['MessageName / SignalName'], int(row['Start Byte']), int(row['Start Bit']), int(row['Length in Bits']) ) )
 

# print(input_csv_data)
# print()
# print()
# print(msg_id_list)
# print()
# print()
# print(msg_name_list)
# print()
# print()
# print(msg_signal_dictionary)
# print()
# print()


# for msg_name in msg_name_list:
#     print( f'Message: {msg_name}')
#     for signal in msg_signal_dictionary[msg_name]:
#         print(f'Signal Name: {signal.signal_name}, Start Byte: {signal.start_byte}, Start Bit: {signal.start_bit}, Length: {signal.length}')



######################################################################################
# Figure out the C callback code needed for each type of signal
#   - For the header file, there's a callback function for each message and that's it.
#   - For the source file, there's a needed C statement for each type of signal with
#     respect to the it's byte/bit placement and length
######################################################################################
can_callbacks_hfile_str = ''
can_callbacks_cfile_str = ''
signal_value_str = ''
# Iterate through the messages obtained and figure out what to do with each signal in the message
for msg_name in msg_name_list:
    # Header file just needs a single callback function declaration for each message
    can_callbacks_hfile_str += f'void {msg_name}_Callback(struct Std_CAN_Queue_Item_S * item);\n\n'

    # Source file needs the function header
    can_callbacks_cfile_str += f'void {msg_name}_Callback(struct Std_CAN_Queue_Item_S * item)\n' + '{\n'
    # Then for each signal in the message, we have a C statement to extract it from the data bytes
    for signal in msg_signal_dictionary[msg_name]:
        if signal.signal_name == 'NA':
            continue

        signal_value_str = ''   # Using a separate string variable to build this C statement to make it easier to bring back in to cfile_str
        
        # Based on signal type, we use a specific C statement
        signal_type = signal.determine_signal_type()

        # Signal is an integer number of bytes long
        if signal_type == SignalType.BYTES_SIGNAL:
            can_callbacks_cfile_str += signal.string_for_bytes_signal()

    
    can_callbacks_cfile_str += '}\n\n'


can_vars_str = ''
for signal_name in signal_name_list:
    can_vars_str += f'CAN_11Bit_{signal_name},\n'


print('\n\nPrinting CAN_11Bit_Vars.h file string:\n')
print(can_vars_str)
with open('CAN_11Bit_Vars.h', 'w') as car_vars_file :
    car_vars_file.write(can_vars_str)


print('\n\nPrinting CAN_11Bit_Callbacks.h file string:\n')
print(can_callbacks_hfile_str)
with open('CAN_11Bit_Callbacks.h', 'w') as can_callbacks_hfile :
    can_callbacks_hfile.write(can_callbacks_hfile_str)


print('\n\nPrinting CAN_11Bit_Callbacks.c file string:\n')
print(can_callbacks_cfile_str)
with open('CAN_11Bit_Callbacks.c', 'w') as can_callbacks_cfile :
    can_callbacks_cfile.write(can_callbacks_cfile_str)