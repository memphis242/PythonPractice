
import csv
from hash_table_generator_functions import unique, StdCAN_HashTableEntry, StdCAN_MessageSignal

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
# Set up needed input data from csv file
with open('StdCANSheet_Updated.csv', 'r', newline='') as csvfile:
    # This DictReader object below can then be iterated over like a list of dictionaries with the column headers as the keys
    csv_reader = csv.DictReader(csvfile)
    
    first_signal_in_msg = True
    # Iterate over the csv_reader object and read in each data dictionary item into the input_csv_data list
    for row in csv_reader:
        input_csv_data.append(row)

        if row['Message / Signal'] == 'M':
            msg_id_list.append(row['MessageID'])
            msg_name_list.append(row['MessageName / SignalName'])
            first_signal_in_msg = True

        else:
            if first_signal_in_msg == True:
                msg_signal_dictionary[msg_name_list[-1]] = []
                first_signal_in_msg = False
            signal_name_list.append( row['MessageName / SignalName'] )
            can_var_name_list.append( f'CAN_11Bit_{ signal_name_list[-1] }' )
            msg_signal_dictionary[msg_name_list[-1]].append( StdCAN_MessageSignal( row['MessageName / SignalName'], int(row['Start Byte']), int(row['Start Bit']), int(row['Length in Bits']) ) )
 

print(input_csv_data)
print()
print()
print(msg_id_list)
print()
print()
print(msg_name_list)
print()
print()
print(msg_signal_dictionary)
print()
print()


for msg_name in msg_name_list:
    print( f'Message: {msg_name}')
    for signal in msg_signal_dictionary[msg_name]:
        print(f'Signal Name: {signal.signal_name}, Start Byte: {signal.start_byte}, Start Bit: {signal.start_bit}, Length: {signal.length}')



can_callbacks_hfile_str = ''
can_callbacks_cfile_str = ''
signal_value_str = ''
for msg_name in msg_name_list:
    can_callbacks_hfile_str += f'void {msg_name}_Callback(struct Std_CAN_Queue_Item_S * item);\n\n'

    can_callbacks_cfile_str += f'void {msg_name}_Callback(struct Std_CAN_Queue_Item_S * item)\n' + '{\n'
    for signal in msg_signal_dictionary[msg_name]:
        signal_value_str = ''
        if signal.length % 8 == 0:
            num_of_bytes = signal.length / 8
            if num_of_bytes == 1:
                signal_value_str += f'(UInt16_T)item->data[{signal.start_byte - 1}]'
            elif num_of_bytes == 2:
                signal_value_str += f'( ( (UInt16_T)item->data[{signal.start_byte}] ) << 8 ) | ( (UInt16_T)item->data[{signal.start_byte - 1}] )'

        can_var_name = f'CAN_11Bit_{signal.signal_name}, '
        can_callbacks_cfile_str += f'\tJD_WriteVarValueStatus( {can_var_name}, {signal_value_str}, DATA_GOODDATA );\n'
    
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