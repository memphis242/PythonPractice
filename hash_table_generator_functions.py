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
class StdCANHashTableEntry:
    relevancy_val: bool
    intended_id: int
    cb: str
    pack_index: int