extended_line_numbers = []

with open( '.\Debug\eCTL_TCU_CRC.hex', 'r', newline='' ) as hex_file:
    lines = hex_file.readlines()
    
    i = 0
    for line in lines:
        i = i + 1
        line_specifier = line[7:9]
        if line_specifier == '04':
            extended_line_numbers.append(i)


print( extended_line_numbers )

