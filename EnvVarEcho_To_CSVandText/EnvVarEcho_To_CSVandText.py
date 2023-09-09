# For working with command-line arguments
import sys

# file_name = 'PATH_08-26-2023.txt'       # For debug run

#########################################################################
# Obtain input file from command-line arguments
#########################################################################
for argument in sys.argv[1:]:
    file_arg = argument.find('--file=')

    # If --file flag was found, extract the filename by removing the "--file" part of the flag.
    if file_arg == 0:
        file_name = argument.replace('--file=','')

    elif file_arg == -1:
        print('ERROR: No file specified')

    else:
        print('ERROR: Please specify the file using --file=<relative_file_path>.')


# Inform of input file...
print(f'Input file is: {file_name}\n')

# Determine validity of file...
if (file_name.find('.txt') == -1):
    raise ValueError('Incorrect file type specified! Needs to be a .txt file.')


#########################################################################
# Open the file, get the line of text, and split by the ';' character.
#########################################################################
print('Parsing the file...\n')
with open(file_name, 'r') as env_var_echo_file:
   input_line = env_var_echo_file.readlines()
   input_line_stripped = input_line[0].strip()
   parsed_paths = input_line_stripped.split(';')


#########################################################################
# Then create a .csv file and a .txt file that include the split string.
#########################################################################
# Use the name of the input log file for the csv file
output_csv_file_name = file_name[0:-4] + '_PARSED.csv'
output_txt_file_name = file_name[0:-4] + '_PARSED.txt'
print(f'Exporting to {output_csv_file_name} and {output_txt_file_name} files...')

with open( output_csv_file_name, 'w', newline='' ) as output_csv_file:
   # Separate rows in a .csv file are identified by newline characters, so this is really no different than the .txt file.
   # I'm just making two files with the same contents but different extensions for convenience's sake.
   for path_name in parsed_paths:
      output_csv_file.write(f'{path_name}\n')

with open( output_txt_file_name, 'w', newline='' ) as output_txt_file:
   for path_name in parsed_paths:
      output_txt_file.write(f'{path_name}\n')

print('Done! :D\n')
