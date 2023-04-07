from dataclasses import dataclass

# Determines if every item in the input list is unique (i.e., there are no repetitions in the list)
def unique(input_list):
    ret_val = True
    for i in input_list:
        if input_list.count(i) > 1:
            ret_val = False
            break
    
    return ret_val


@dataclass
class StdCAN_HashTableEntry:
    relevancy_val: bool
    intended_id: int
    cb: str
    pack_index: int


@dataclass
class StdCAN_MessageSignal:
    signal_name: str
    start_byte: int
    start_bit: int
    length: int     # in bits