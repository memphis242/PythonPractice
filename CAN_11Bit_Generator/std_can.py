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


class StdCAN_MessageSignal:
    """Class to represent the Standard CAN Message Signal"""

    # Class parameters shared by all instances of this class
    NUM_OF_BITS_PER_BYTE = 8
    NUM_OF_BYTES_PER_MESSAGE = 8
    SINGLE_BIT_MASK_TABLE =     { 1: '0x01', 2: '0x02', 3: '0x04', 4: '0x08', 5: '0x10', 6: '0x20', 7: '0x40', 8: '0x80' }
    TWO_BIT_MASK_TABLE =        { 1: '0x03', 2: '0x06', 3: '0x0C', 4: '0x18', 5: '0x30', 6: '0x60', 7: '0xC0' }
    THREE_BIT_MASK_TABLE =      { 1: '0x07', 2: '0x0E', 3: '0x1C', 4: '0x38', 5: '0x70', 6: '0xE0' }
    FOUR_BIT_MASK_TABLE =       { 1: '0x0F', 2: '0x1E', 3: '0x3C', 4: '0x78', 5: '0xF0' }
    BIT_MASK_DICTIONARY = { 1: SINGLE_BIT_MASK_TABLE, 2: TWO_BIT_MASK_TABLE, 3: THREE_BIT_MASK_TABLE, 4: FOUR_BIT_MASK_TABLE }
    MSB_BIT_MASK_TABLE = { 0: '0x00', 1: '0x01', 2: '0x03', 3: '0x07', 4: '0x0F', 5: '0x1F', 6: '0x3F', 7: '0x7F', 8: '0xFF' }

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
        c_statement_str = ''

        # Obtain number of bytes of signal
        num_of_bytes = int(self.length / self.NUM_OF_BITS_PER_BYTE)

        # Simplest case
        if num_of_bytes == 1:
            signal_value_str += f'(JD_VARMNGR_OBJ)item->data[{self.start_byte - 1}]'

        # Need to use bitwise OR to get full signal from here on out
        elif num_of_bytes == 2:
            signal_value_str += f'( (JD_VARMNGR_OBJ)item->data[{self.start_byte - 1}] ) | ( ( (JD_VARMNGR_OBJ)item->data[{self.start_byte}] ) << 8 )'

        elif num_of_bytes == 3:
            signal_value_str_upper = f'(JD_VARMNGR_OBJ)item->data[{self.start_byte + 1}]'
            signal_value_str_lower = f'( (JD_VARMNGR_OBJ)item->data[{self.start_byte - 1}] ) | ( ( (JD_VARMNGR_OBJ)item->data[{self.start_byte}] ) << 8 ) '

        elif num_of_bytes == 4:
            signal_value_str_upper = f'( (JD_VARMNGR_OBJ)item->data[{self.start_byte + 1}] ) | ( ( (JD_VARMNGR_OBJ)item->data[{self.start_byte + 2}] ) << 8 ) '
            signal_value_str_lower = f'( (JD_VARMNGR_OBJ)item->data[{self.start_byte - 1}] ) | ( ( (JD_VARMNGR_OBJ)item->data[{self.start_byte}] ) << 8 ) '

        else:
            print(f'WARNING: Signal length of {self.length} bits not supported')
            signal_value_str += f'// Signal {self.signal_name} has a length of {self.length} that is not supported. Sorry.\n'

        if num_of_bytes <= 2:
            can_var_name = f'CAN_11Bit_{self.signal_name}'
            c_statement_str += f'\tJD_WriteVarValueStatus( {can_var_name}, {signal_value_str}, DATA_GOODDATA );\n'
        
        elif num_of_bytes > 2 and num_of_bytes <= 4:
            can_var_name_upper = f'CAN_11Bit_{self.signal_name}_Upper'
            can_var_name_lower = f'CAN_11Bit_{self.signal_name}_Lower'
            c_statement_str += f'\tJD_WriteVarValueStatus( {can_var_name_upper}, {signal_value_str_upper}, DATA_GOODDATA );\n'
            c_statement_str += f'\tJD_WriteVarValueStatus( {can_var_name_lower}, {signal_value_str_lower}, DATA_GOODDATA );\n'

        return c_statement_str


    # Return string that corresponds to the kind of C statement that would obtain
    # the data for this signal.
    def string_for_contained_bits(self) -> str:
        signal_value_str = ''
        c_statement_str = ''

        # Check for validity first
        if self.length > 4:
            print('WARNING: Byte-contained signals that are greater than 4 bits in length are currently not supported!')
            c_statement_str = '// WARNING: Byte-contained signals that are greater than 4 bits in length are currently not supported!\n'
            
        else:
            bit_mask = self.BIT_MASK_DICTIONARY[self.length][self.start_bit]
            # If start bit is the LSb, no need for shifting
            if self.start_bit == 1:
                signal_value_str += f'( (JD_VARMNGR_OBJ)item->data[{self.start_byte - 1}] & {bit_mask} )'
            # Otherwise, shifting is required
            else:
                signal_value_str += f'( ( (JD_VARMNGR_OBJ)item->data[{self.start_byte - 1}] & {bit_mask} ) >> {self.start_bit - 1} )'
            can_var_name = f'CAN_11Bit_{self.signal_name}'
            c_statement_str = f'\tJD_WriteVarValueStatus( {can_var_name}, {signal_value_str}, DATA_GOODDATA );\n'

        return c_statement_str


    # Return string that corresponds to the kind of C statement that would obtain
    # the data for this signal.
    def string_for_bits_signal_multibyte(self) -> str:
        signal_value_str = ''
        c_statement_str = ''

        if ( self.start_bit + self.length ) > 16:
            print('WARNING: Multi-byte signals that are not divisible in length by 8 and span more than two bytes are NOT supported. Get that ugliness away from here.')
            c_statement_str += '// WARNING: Multi-byte signals that are not divisible in length by 8 and span more than two bytes are NOT supported. Get that ugliness away from here.'

        # We should only get to this point if the signal length is more than 8 but spans no more than 2 bytes
        # This means we're dealing with bits in a Most Significant Byte (MSB) and a Least Significant Byte (LSB)
        else:
            # Determine number of bits in LSB
            lsb_num_of_bits = self.NUM_OF_BITS_PER_BYTE - (self.start_bit - 1)
            # Determine number of unrelated bits in LSB
            lsb_num_of_unrelated_bits = self.start_bit - 1
            # Determine number of bits in MSB
            msb_num_of_bits = self.length - lsb_num_of_bits
            # Obtain masks for MSB and LSB
            msb_bit_mask = self.MSB_BIT_MASK_TABLE[msb_num_of_bits]
            # Neat trick to get those upper bits. I'm basically doing ( 0xFF & ~MSB_LUT[start_bit - 1] ).
            # This goes off the realization that from start bit to the MSb of this LSB, we'll need all 1's for the mask.
            lsb_bit_mask = hex( int( '0xFF', 16 ) & ( int(self.MSB_BIT_MASK_TABLE[self.start_bit - 1], 16) ^ int( '0xFF', 16 ) ) ).upper().replace('X', 'x')

            # Okay, we have everything we need!
            signal_value_str += f'( ( (JD_VARMNGR_OBJ)item->data[{self.start_byte - 1}] & {lsb_bit_mask} ) >> {lsb_num_of_unrelated_bits} ) | ( ( (JD_VARMNGR_OBJ)item->data[{self.start_byte}] & {msb_bit_mask} ) << {lsb_num_of_bits} )'
            can_var_name = f'CAN_11Bit_{self.signal_name}'
            c_statement_str = f'\tJD_WriteVarValueStatus( {can_var_name}, {signal_value_str}, DATA_GOODDATA );\n'
        

        return c_statement_str
        




# Determines if every item in the input list is unique (i.e., there are no repetitions in the list)
def unique(input_list):
    ret_val = True
    for i in input_list:
        if input_list.count(i) > 1:
            ret_val = False
            break
    
    return ret_val
