import sys

# See if relative path can be specified for file...
# Read in inputs that should be specified with corresponding flags.
for argument in sys.argv[1:]:
    file_arg = argument.find('--file=')
    if file_arg == 0:
        file_name = argument.replace('--file=','')

    elif file_arg == -1:
        print('ERROR: No file specified')

    else:
        print('ERROR: Please specify the file using --file=<relative_file_path>.')

with open(file_name, 'r') as argv_file:
    print()
    print(argv_file.read())
    print()
