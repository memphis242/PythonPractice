import csv
from hash_table_generator_functions import unique, StdCANHashTableEntry

print('\nRunning the hash_table_generator.py script to compute an appropriate value\n\
to be used in the receive hash function as well as the hash table for 11-bit CAN receives.\n\
The hash function will be of the form: <message_id> % <value> = <hash_value>.\n')

#########################################################################
# Read in CSV data
#########################################################################
print('\t\tObtaining data from csv file...')

input_csv_data = []     # This variable will hold the list of dictionaries, where each dictionary represents a row
input_msg_id_data = []  # This list will hold the message IDs in the sheet, which turns out to be convenient later on
# Set up needed input data from csv file
with open('StdCANSheet.csv', 'r', newline='') as csvfile:
    # This DictReader object below can then be iterated over like a list of dictionaries with the column headers as the keys
    csv_reader = csv.DictReader(csvfile)
    
    # Iterate over the csv_reader object and read in each data dictionary item into the input_csv_data list
    for row in csv_reader:
        input_csv_data.append(row)
        input_msg_id_data.append(row['MessageID'])



#########################################################################
# Compute appropriate value for hash function
#   Find the smallest hash function value (so that we get a small hash table)
#   that is hopefully also a power of two (so we don't have to divide).
#########################################################################
print('\t\tComputing value for hash function...')

MAX_HASH_FUNCTION_VALUE = int( max(input_msg_id_data) )     # Uncomment this line if you want to guarantee the smallest number that produces no collisions
# MAX_HASH_FUNCTION_VALUE = 2 ** 11 - 1     # Uncomment this line if you want better odds that a power of two will be found
print( '\t\t\tMaximum hash function value based on input list: {}'.format(MAX_HASH_FUNCTION_VALUE) )

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
hash_function_value = len(input_csv_data)
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
    for row in input_csv_data:
        hash_values_list.append( int(row['MessageID']) % hash_function_value )
    
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
#   The hash table will be a list of StdCANHashTableEntry objects. I'm going
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
    hash_table.append( StdCANHashTableEntry(0, 0, 'NULL', 0) )

# Now for the relevant indices, fill them up with the respective data.
# Remember, the way the hash table works is we take the message ID, perform
# the hash function (which is just ID modulo hash_function_value), and use
# the result to index into the hash_table and find any relevant information
# we want (refer to this section's header comment ^).
for message in input_csv_data:
    hash_table_idx = int(message['MessageID']) % hash_function_value
    hash_table[hash_table_idx] = StdCANHashTableEntry( True, int(message['MessageID']), f"{message['MessageName']}_Callback", int(message['PackIndex']) )

# for entry in hash_table:
#     print(entry)



#########################################################################
# Make the file strings
#########################################################################
print('\t\tMaking the file strings...')

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
hash_table_file_str += '#include "StdCANHashValue.h\n#include "ExternalMaster_Callbacks.h"\n'

# Useful comment when looking at this file
hash_table_file_str += \
'''\n\n/* Recall that Relevancy_Table_Item struct has members:
*\t\t- UInt8_T relevancy_val
*\t\t- UInt16_T intended_id
*\t\t- void (* cb)(struct Std_CAN_Queeu_Item_S * item)
*\t\t- UInt8_T pack_index */\n\n'''

# Declare hash table
hash_table_file_str += 'const struct Relevancy_Table_Item RELEVANCY_HASH_TABLE[STD_QUEUE_HASH_NUM] = \n{\n'

# Fill 'er up!
for idx, entry in enumerate(hash_table) :
    hash_table_file_str +=\
        '\t{{\t{:1},\t\t{:4},\t\t{},\t\t{:2}\t}}'.format(str(entry.relevancy_val), str(entry.intended_id), str(entry.cb), str(entry.pack_index) )
    if idx < hash_function_value :    # Only place commas after the items that are not the last item
        hash_table_file_str += ',\n'
hash_table_file_str += '\n};'


## Now the callback function header file
callback_file_str = \
'''/**********************************************************************************************************/
/***** AUTOGENERATED from git@github.deere.com:Construction-BatteryElectricVehicle/ExternalMaster.git *****/
/**********************************************************************************************************/

'''
# Header file include protection
callback_file_str += \
'''#ifndef EXM_CALLBACKS_H
#define EXM_CALLBACKS_H

'''
# Any necessary includes
callback_file_str += \
'''#include "HWCONFIG.H"
#include "CAN_StandardCAN_DS.h"

'''
# External declarations
callback_file_str += 'extern struct Std_CAN_Queue_Item_S;\n\n'
# Fill 'er up!
callback_file_str += '\n/** Function Declarations **/\n'
# In order to prevent a callback function name from being used more than once,
# I will record whether or not a given callback function name has been used already
# or not. And it looks like that's probably fastest done using another hash table! :D
# How fitting! I will make a data dictionary whose keys are the callback function
# names from the hash table (except for any 'NULL' names), and the value at each location
# will be a bool False or True to represent whether that name has been used or not.
# next_callback_name = hash_table[0].cb   # This variable will hold the next callback name to be used
name_table = {}
# Initialize hash table for names
for entry in hash_table:
    if entry.cb != 'NULL':
        name_table[entry.cb] = False
# Now iterate through the hash table, and if the callback function name has not been
# used yet, make a line in the callback_file_str for that callback function.
for entry in hash_table:
    # If the callback function name is 'NULL' or has already been used, skip it.
    if entry.cb == 'NULL' or name_table[entry.cb] == True:
        continue
    # Otherwise, use the name and mark it as used in the name table
    callback_file_str += 'void {}(struct Std_CAN_Queue_Item_S * item);\n\n'.format(entry.cb)
    name_table[entry.cb] = True
    
# Header file include protection footer
callback_file_str += '\n\n#endif\t\t// EXM_CALLBACKS_H'


#########################################################################
# Write to files
#########################################################################
print('\t\tFinally, writing to output files to be used in handcode...')

with open('StdCANHashTable.c', 'w') as hash_table_file :
    hash_table_file.write(hash_table_file_str)

with open('StdCANHashValue.h', 'w') as hash_function_value_file :
    hash_function_value_file.write(hash_function_value_file_str)

with open('ExternalMaster_Callbacks.h', 'w') as callbacks_file :
    callbacks_file.write(callback_file_str)
