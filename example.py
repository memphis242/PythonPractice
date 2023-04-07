from hash_table_generator_functions import StdCAN_MessageSignal

# example_list = [1, 2, 3, 'String']
# print(example_list[0])
# 
# example_dictionary = { 101: True, 102: False, 103: False } 
# print(example_dictionary[101])
# 
# 
# for i in range(10):
#     print(i)
# 

example_dictionary_of_lists = {}
example_dictionary_of_lists['VoltageMessage'] = [StdCAN_MessageSignal('Pack1Voltage', 1, 1, 16)]
example_dictionary_of_lists['VoltageMessage'].append(StdCAN_MessageSignal('Pack1Current', 3, 1, 16))
example_dictionary_of_lists['VoltageMessage'].append(StdCAN_MessageSignal('Pack1DCBusVoltage', 5, 1, 16))
example_dictionary_of_lists['CellVoltageMessage'] = [StdCAN_MessageSignal('Pack1Voltage', 1, 1, 16)]
example_dictionary_of_lists['CellVoltageMessage'].append(StdCAN_MessageSignal('Pack1Current', 3, 1, 16))
example_dictionary_of_lists['CellVoltageMessage'].append(StdCAN_MessageSignal('Pack1DCBusVoltage', 5, 1, 16))
print(example_dictionary_of_lists)
