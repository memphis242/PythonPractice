
# For working with the input sheets:
import csv
import pandas as pd
# For my custom functions / class definition
from std_can import unique, \
                    StdCAN_HashTableEntry, StdCAN_MessageSignal, SignalType


# Constants for the whole file
CALLBACK_HEADER_FILE_NAME = 'CAN_11Bit_Callback.h'
CALLBACK_SOURCE_FILE_NAME = 'CAN_11Bit_Callback.c'
CAN_VARS_HEADER_FILE_NAME = 'CAN_11Bit_Vars.h'
HASH_TABLE_VALUE_HEADER_FILE_NAME = 'CAN_11Bit_RxHashValue.h'
HASH_TABLE_SOURCE_FILE_NAME = 'CAN_11Bit_RxHashTable.c'
INPUT_EXCEL_FILE_NAME = 'StdCANSheet_Updated.xlsx'
OUTPUT_CSV_FILE_NAME = INPUT_EXCEL_FILE_NAME.replace('xlsx', 'csv')



# Print initial display message...
print('\nRunning std_can_catg.py to generate 11-bit CAN app-vars, header/source files for callback functions, and Rx hash table/value files...\n')

#########################################################################
# Convert .xlsx Sheet into .csv File
# NOTE: Unforuntately, one annoying thing about the pandas conversion of
#       .xlsx into .csv is it seems to take numbers from the .xslx and
#       print them as decimal-point numbers (floats) in the .csv.
#########################################################################
print('\t\tConverting .xlsx input file into .csv file...')
xlsx_file = pd.read_excel(INPUT_EXCEL_FILE_NAME)
xlsx_file.to_csv(OUTPUT_CSV_FILE_NAME, index=None, header=True)


#########################################################################
# Read in CSV data
#########################################################################
print('\t\tObtaining data from csv file...')

input_csv_data = []     # This variable will hold the list of dictionaries, where each dictionary represents a row
msg_id_list = []        # This list will hold the message IDs in the sheet, which turns out to be convenient later on
msg_name_list = []
signal_name_list = []
can_var_name_list = []
msg_signal_dictionary = {}
# Read in data from csv file into local object
with open(OUTPUT_CSV_FILE_NAME, 'r', newline='') as csvfile:
    # This DictReader object below can then be iterated over like a list of dictionaries with the column headers as the keys
    csv_reader = csv.DictReader(csvfile)
    
    for row in csv_reader:
        input_csv_data.append(row)

# Get information from input data
first_signal_in_msg = True
for idx, row in enumerate(input_csv_data):

    if row['Message / Signal'] == 'M':

        msg_id_list.append(int(float(row['MessageID'])))
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
        can_var_name_list.append( f'CAN_11Bit_{ signal_name_list[-1] }' )   # The template for CAN app-vars will be "CAN_11Bit_<signal name>"
        msg_signal_dictionary[msg_name_list[-1]].append( StdCAN_MessageSignal( row['MessageName / SignalName'], int(float(row['Start Byte'])), int(float(row['Start Bit'])), int(float(row['Length in Bits'])) ) )
 


######################################################################################
# Figure out the C callback code needed for each type of signal. It will be one callback
# function per message, where a message may contain multiple signals.
#   - For the header file, there's a callback function for each message and that's it.
#   - For the source file, there's a needed C statement for each type of signal with
#     respect to the it's byte/bit placement and length
######################################################################################
print('\t\tFiguring out the callback function code for each of these messages...')
can_callbacks_hfile_str = ''
can_callbacks_cfile_str = ''
can_vars_str = ''
callback_function_list = []
# Iterate through the messages obtained and figure out what to do with each signal in the message
for msg_name in msg_name_list:
    callback_function_list.append(f'{msg_name}_Callback')
    # Header file just needs a single callback function declaration for each message
    can_callbacks_hfile_str += f'void {callback_function_list[-1]}(struct Std_CAN_Queue_Item_S * item);\n\n'

    # Source file needs the function header
    can_callbacks_cfile_str += f'void {callback_function_list[-1]}(struct Std_CAN_Queue_Item_S * item)\n' + '{\n'
    # Then for each signal in the message, we have a C statement to extract it from the data bytes
    for signal in msg_signal_dictionary[msg_name]:
        if signal.signal_name == 'NA':
            continue

        # Based on signal type, we use a specific C statement
        signal_type = signal.determine_signal_type()

        # Signal is an integer number of bytes long
        if signal_type == SignalType.BYTES_SIGNAL:
            can_callbacks_cfile_str += signal.string_for_bytes_signal()

        # Signal is less than a byte long and is contained
        if signal_type == SignalType.BITS_SIGNAL_LESS_THAN_A_BYTE_CONTAINED:
            can_callbacks_cfile_str += signal.string_for_contained_bits()

        if signal_type == SignalType.BITS_SIGNAL_MORE_THAN_A_BYTE:
            can_callbacks_cfile_str += signal.string_for_bits_signal_multibyte()

        # Now the CAN_11Bit_Vars.h str
        num_of_bytes = signal.length / StdCAN_MessageSignal.NUM_OF_BITS_PER_BYTE 
        if num_of_bytes <= 2:
            can_vars_str += f'CAN_11Bit_{signal.signal_name},\n'
        
        elif num_of_bytes <= 4:
            can_vars_str += f'CAN_11Bit_{signal.signal_name}_Upper,\n'
            can_vars_str += f'CAN_11Bit_{signal.signal_name}_Lower,\n'

    # Function footer
    can_callbacks_cfile_str += '}\n\n'



#########################################################################
# Compute appropriate value for hash function
#   Find the smallest hash function value (so that we get a small hash table)
#   that is hopefully also a power of two (so we don't have to divide).
#########################################################################
print('\t\tNow computing value for hash function...')

MAX_HASH_FUNCTION_VALUE = int( max(msg_id_list) )     # Uncomment this line if you want to guarantee the smallest number that produces no collisions
# MAX_HASH_FUNCTION_VALUE = 2 ** 11 - 1     # Uncomment this line if you want better odds that a power of two will be found
print(f'\t\t\tMaximum hash function value based on input list: {MAX_HASH_FUNCTION_VALUE}')

# It would be really convenient if the hash function value was a power of two.
# This is because instead of a division operation for the hash function, a simple
# AND operation is done instead! Which is way better for speed. In order to check
# if the hash function value is a power of two, I will just make a list of the powers
# of two up to the maximum power of two that 11-bits can hold --> 2^10.
powers_of_two_list = []
for i in range(1,11):
    powers_of_two_list.append(2 ** i)

# Starting guess for the hash function value will be the length of the list
# (the hash function value has to be greater than or equal to this value no matter what)
hash_function_value = len(msg_id_list)
print( '\t\t\tStarting guess for hash function value: {}'.format(hash_function_value) )
# Other relevant variables for this computation...
smallest_hash_function_value = None
smallest_hash_function_value_has_been_set = False
all_hash_values_are_unique = False
hash_function_value_is_power_of_two = False
hash_values_list = []
# We will keep looping through possible hash function values until the value produces no collisions
# and is a power of two. If after iterating through all possible values the resulting hash function
# value is NOT a power of two, then instead we will just use the smallest hash function value that
# produced no collisions
while ( all_hash_values_are_unique == False or hash_function_value_is_power_of_two == False ) and\
        hash_function_value <= MAX_HASH_FUNCTION_VALUE:
    # Perform the hash function on each message ID to get a list of hash values produced
    # from this particular has function value
    for msg_id in msg_id_list:
        hash_values_list.append( int(msg_id) % hash_function_value )
    
    # Determine if this hash function value produced resulted in no collisions...
    all_hash_values_are_unique = unique(hash_values_list)

    # Determine if the hash function value is a power of two
    hash_function_value_is_power_of_two = hash_function_value in powers_of_two_list

    # If no collisions were produced and this is the first time this has happened, record this
    # hash function value to keep track of this, as it will be the smallest hash function value
    if all_hash_values_are_unique == True and smallest_hash_function_value_has_been_set == False:
        smallest_hash_function_value = hash_function_value
        smallest_hash_function_value_has_been_set = True

    # If there were collisions, then go to the next hash function value to test, which
    # for now will just be the current value += 1. This loop is guaranteed to stop at
    # max(message ids in list), since that will obviously produce no collisions.
    if all_hash_values_are_unique == False:
        hash_function_value += 1
        hash_values_list = []   # Reset the list that we check for collisions

# If we exited the loop because we couldn't find a hash function value that was BOTH a power of two
# AND resulted in no collisions, then we'll just use the smallest hash function value that resulted
# in no collisions
if all_hash_values_are_unique == False or hash_function_value_is_power_of_two == False:
    hash_function_value = smallest_hash_function_value
print( '\t\t\tHash function value found: {}'.format(hash_function_value) )




#########################################################################
# Create the hash table
#   The hash table will be a list of StdCAN_HashTableEntry objects. I'm going
#   with that instead of a dictionary because I prefer having the defined
#   structure.
#   Also, note that the size of the hash table will be hash_function_value.
#   The structure of table is as follows. Each row contains a:
#       - relevancy_val : A boolean value that indicates whether the message ID
#                         that mapped here was indeed relevant (i.e., in the CAN sheet).
#       - intended_id   : The ID that was intended to get mapped to this location in
#                         the table. This is how I deal with collisions.
#       - cb            : This is the callback function that will be associated with
#                         with this message ID.
#       - pack_index    : This is the pack index that corresponds to this message ID.
#                         This information comes from the CAN sheet.
#########################################################################

print('\t\tCreating hash table...')

# Create a list of empty objects of size hash_function_value
hash_table = []
for i in range(hash_function_value):
    hash_table.append( StdCAN_HashTableEntry(0, 0, 'NULL') )

# Now for the relevant indices, fill them up with the respective data.
# Remember, the way the hash table works is we take the message ID, perform
# the hash function (which is just ID modulo hash_function_value), and use
# the result to index into the hash_table and find any relevant information
# we want (refer to this section's header comment ^).
for msg_id in msg_id_list:
    hash_table_idx = int(msg_id) % hash_function_value
    hash_table[hash_table_idx].intended_id = msg_id
    hash_table[hash_table_idx].relevancy_val = True

for idx, cb_name in enumerate(callback_function_list):
    hash_table_idx = int(msg_id_list[idx]) % hash_function_value
    hash_table[hash_table_idx].cb = cb_name



#########################################################################
# Make the file strings
#########################################################################
print('\t\tNow making the rx hash table file strings...')

## First the hash function value header file
hash_function_value_file_str = \
'''/**********************************************************************************************************/
/***** AUTOGENERATED from git@github.deere.com:Construction-BatteryElectricVehicle/ExternalMaster.git *****/
/**********************************************************************************************************/

'''
# Header file include protection
hash_function_value_file_str += \
'''#ifndef STD_CAN_HASH_VALUE_H
#define STD_CAN_HASH_VALUE_H

'''
# Hash value macro define
hash_function_value_file_str += f'#define STD_QUEUE_HASH_NUM\t{hash_function_value}\n'
# Heder file protection footer
hash_function_value_file_str += '\n#endif\t\t// STD_CAN_HASH_VALUE_H'


## Now the hash table source file
hash_table_file_str = \
'''/**********************************************************************************************************/
/***** AUTOGENERATED from git@github.deere.com:Construction-BatteryElectricVehicle/ExternalMaster.git *****/
/**********************************************************************************************************/

'''
# Necessary includes
hash_table_file_str += f'#include "{HASH_TABLE_VALUE_HEADER_FILE_NAME}"\n#include "{CALLBACK_HEADER_FILE_NAME}"\n'

# Useful comment when looking at this file
hash_table_file_str += \
'''\n\n/* Recall that Relevancy_Table_Item struct has members:
*\t\t- UInt8_T relevancy_val
*\t\t- UInt16_T intended_id
*\t\t- void (* cb)(struct Std_CAN_Queeu_Item_S * item) */\n\n'''

# Declare hash table
hash_table_file_str += 'const struct Relevancy_Table_Item RELEVANCY_HASH_TABLE[STD_QUEUE_HASH_NUM] = \n{\n'

# Fill 'er up!
for idx, entry in enumerate(hash_table) :
    hash_table_file_str +=\
        '\t{{\t{:1},\t\t{:4},\t\t{}\t}}'.format(str(int(bool(entry.relevancy_val))), str(entry.intended_id), str(entry.cb) )
    if idx < hash_function_value :    # Only place commas after the items that are not the last item
        hash_table_file_str += ',\n'
hash_table_file_str += '\n};'


# ## Now the callback function header file
# callback_file_str = \
# '''/**********************************************************************************************************/
# /***** AUTOGENERATED from git@github.deere.com:Construction-BatteryElectricVehicle/ExternalMaster.git *****/
# /**********************************************************************************************************/
# 
# '''
# # Header file include protection
# callback_file_str += \
# '''#ifndef EXM_CALLBACKS_H
# #define EXM_CALLBACKS_H
# 
# '''
# # Any necessary includes
# callback_file_str += \
# '''#include "HWCONFIG.H"
# #include "CAN_StandardCAN_DS.h"
# 
# '''
# # External declarations
# callback_file_str += 'extern struct Std_CAN_Queue_Item_S;\n\n'
# # Fill 'er up!
# callback_file_str += '\n/** Function Declarations **/\n'
#
# # Header file include protection footer
# callback_file_str += '\n\n#endif\t\t// EXM_CALLBACKS_H'


#########################################################################
# Write to files
#########################################################################
print('\t\tFinally, writing to output files to be used in handcode...')

with open(HASH_TABLE_SOURCE_FILE_NAME, 'w') as hash_table_file :
    hash_table_file.write(hash_table_file_str)

with open(HASH_TABLE_VALUE_HEADER_FILE_NAME, 'w') as hash_function_value_file :
    hash_function_value_file.write(hash_function_value_file_str)

with open(CAN_VARS_HEADER_FILE_NAME, 'w') as car_vars_file :
    car_vars_file.write(can_vars_str)

with open(CALLBACK_HEADER_FILE_NAME, 'w') as can_callbacks_hfile :
    can_callbacks_hfile.write(can_callbacks_hfile_str)

with open(CALLBACK_SOURCE_FILE_NAME, 'w') as can_callbacks_cfile :
    can_callbacks_cfile.write(can_callbacks_cfile_str)