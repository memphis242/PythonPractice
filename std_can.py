from dataclasses import dataclass
from enum import Enum


# Defines an enumeration for the type of signals that might appear in a message
# with respect to the placement of bits/bytes and length
class SignalType(Enum):
    BYTES_SIGNAL                            = 1     # Number of bits is divisible by 8, which is to say the signal is 1 or more full bytes in length
    BITS_SIGNAL_LESS_THAN_A_BYTE_CONTAINED  = 2     # Number of bits is less than 8 and signal is contained in a single byte
    BITS_SIGNAL_LESS_THAN_A_BYTE_SPILLS     = 3     # Number of bits is less than 8 but spills past the border of a byte
    BITS_SIGNAL_MORE_THAN_A_BYTE            = 4     # Number of bits is greater than 8 and not divisible by 8
    SIGNAL_UNDEFINED                        = 5
    

@dataclass
class StdCAN_HashTableEntry:
    relevancy_val: bool
    intended_id: int
    cb: str
    pack_index: int


class StdCAN_MessageSignal:
    """Class to represent the Standard CAN Message Signal"""

    # Class parameters shared by all instances of this class
    NUM_OF_BITS_PER_BYTE = 8
    NUM_OF_BYTES_PER_MESSAGE = 8

    # Constructor
    def __init__(self, signal_name: str, start_byte: int, start_bit: int, length: int):
        self.signal_name = signal_name
        self.start_byte = start_byte
        self.start_bit = start_bit
        self.length = length


    # Determine type of signal with respect to its bit/byte positioning and length
    def determine_signal_type(self) -> SignalType:
        # Default signal type unless proven otherwise
        signal_type = SignalType.SIGNAL_UNDEFINED

        # Check signal validity first
        if self.length > 0 and self.start_bit <= self.NUM_OF_BITS_PER_BYTE and \
            self.start_byte <= self.NUM_OF_BYTES_PER_MESSAGE:

            # If divisible by 8, means it's a signal that's an integer number of bytes long
            if self.length % self.NUM_OF_BITS_PER_BYTE == 0:
                signal_type = SignalType.BYTES_SIGNAL

            # Check if signal spans more than one byte
            elif self.length > self.NUM_OF_BITS_PER_BYTE:
                signal_type = SignalType.BITS_SIGNAL_MORE_THAN_A_BYTE

            # Check if signal is contained in a byte
            elif ( self.start_bit + self.length ) <= self.NUM_OF_BITS_PER_BYTE:
                signal_type = SignalType.BITS_SIGNAL_LESS_THAN_A_BYTE_CONTAINED

            # Only other option left is for signal to cross a byte border but be less than 8 bits long
            else:
                signal_type = SignalType.BITS_SIGNAL_LESS_THAN_A_BYTE_SPILLS

        return signal_type


    # Return string that corresponds to the kind of C statement that would obtain
    # the data for this signal.
    # NOTE: It is assumed that the signal is placed in the message LSB first
    def string_for_bytes_signal(self) -> str:
        signal_value_str = ''

        # Obtain number of bytes of signal
        num_of_bytes = int(self.length / 8)

        # Simplest case
        if num_of_bytes == 1:
            signal_value_str += f'(UInt16_T)item->data[{self.start_byte - 1}]'

        # Need to use bitwise OR to get full signal from here on out
        elif num_of_bytes == 2:
            signal_value_str += f'( (UInt16_T)item->data[{self.start_byte - 1}] ) | ( ( (UInt16_T)item->data[{self.start_byte}] ) << 8 )'

        elif num_of_bytes == 3:
            signal_value_str_upper = f'(UInt16_T)item->data[{self.start_byte + 1}]'
            signal_value_str_lower = f'( (UInt16_T)item->data[{self.start_byte - 1}] ) | ( ( (UInt16_T)item->data[{self.start_byte}] ) << 8 ) '

        elif num_of_bytes == 4:
            signal_value_str_upper = f'( (UInt16_T)item->data[{self.start_byte + 1}] ) | ( ( (UInt16_T)item->data[{self.start_byte + 2}] ) << 8 ) '
            signal_value_str_lower = f'( (UInt16_T)item->data[{self.start_byte - 1}] ) | ( ( (UInt16_T)item->data[{self.start_byte}] ) << 8 ) '

        else:
            print(f'Warning!\tSignal length of {self.length} bits not supported')
            signal_value_str += f'// Signal {self.signal_name} has a length of {self.length} that is not supported. Sorry.'

        c_statement_str = ''
        if num_of_bytes <= 2:
            can_var_name = f'CAN_11Bit_{self.signal_name}'
            c_statement_str += f'\tJD_WriteVarValueStatus( {can_var_name}, {signal_value_str}, DATA_GOODDATA );\n'
        
        elif num_of_bytes > 2 and num_of_bytes < 4:
            can_var_name_upper = f'CAN_11Bit_{self.signal_name}_Upper'
            can_var_name_lower = f'CAN_11Bit_{self.signal_name}_Lower'
            c_statement_str += f'\tJD_WriteVarValueStatus( {can_var_name_upper}, {signal_value_str_upper}, DATA_GOODDATA );\n'
            c_statement_str += f'\tJD_WriteVarValueStatus( {can_var_name_lower}, {signal_value_str_lower}, DATA_GOODDATA );\n'

        return c_statement_str





# Determines if every item in the input list is unique (i.e., there are no repetitions in the list)
def unique(input_list):
    ret_val = True
    for i in input_list:
        if input_list.count(i) > 1:
            ret_val = False
            break
    
    return ret_val
