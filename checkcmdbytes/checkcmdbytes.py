import csv
import sys

# INPUT_CSV_FILE_NAME = './checkcmdbytes/eCTL_CANSheet.csv'
INPUT_CSV_FILE_NAME = 'eCTL_CANSheet.csv'
PGN_COLUMN = 2
PGN_COLUMN_HEADER = 'PGN/SPN'
CMD_BYTE_COLUMN = 7
CMD_BYTE_COLUMN_HEADER = 'Command Bytes'
FLAGS_COLUMN = 1
FLAGS_COLUMN_HEADER = 'Flags'


input_cmd_byte = sys.argv[1]
if not input_cmd_byte:
   print('No command byte specified!')

input_csv_data = []
proprietary_pgn_taken_command_bytes = []
with open(INPUT_CSV_FILE_NAME, 'r', newline='') as csvfile:
   # This DictReader object below can then be iterated over like a list of dictionaries with the column headers as the keys
   csv_reader = csv.DictReader(csvfile)

   for idx, row in enumerate(csv_reader):
      if row['Flags'] == 'PGN' and row['PGN/SPN'] == '61184':
         proprietary_pgn_taken_command_bytes.append( row['Command Bytes'] )

proprietary_pgn_taken_command_bytes.sort()
print('Proprietary A Message (61184 or 0xEF00) Command Bytes That Are Taken:')
for cmd_byte in proprietary_pgn_taken_command_bytes:
   print(f'\t{cmd_byte}')

input_cmd_byte_taken = input_cmd_byte in proprietary_pgn_taken_command_bytes
print(f'\nIs {input_cmd_byte} taken?\t{input_cmd_byte_taken}')