import sys, os, fnmatch

def find( pattern, path ):
   result = []
   for root, dirs, files in os.walk(path):
      for name in files:
         # print( name )
         if fnmatch.fnmatch(name, pattern):
            result.append(os.path.join(root, name))
      break    # Don't want to recursive into subfolders
   return result

#########################################################################
# Obtain the file pattern to search for from command-line arguments
#########################################################################
pattern_to_search = sys.argv[1]
if not pattern_to_search:
   print('No pattern specified!')


#########################################################################
# Search for pattern in PATH variable
#########################################################################
# Read in PATH variable
PATH_ENV_VAR = os.environ['PATH']
# Split PATH var based on ';' and create a list accordingly for easier iteration through each path specified
parsed_paths_list = PATH_ENV_VAR.split(';')
# Search through paths specified for the pattern of interest
list_of_matches = []
for path in parsed_paths_list:
   search_result = find( pattern_to_search, path ) 
   if search_result and (search_result not in list_of_matches) :
      list_of_matches.append(search_result)
# Print out the results
for item in list_of_matches:
   print(item[0])



# RESOURCES USED
# https://stackoverflow.com/questions/1724693/find-a-file-in-python
# https://docs.python.org/3/library/os.html#files-and-directories
# https://stackoverflow.com/questions/4117588/non-recursive-os-walk
# https://stackoverflow.com/questions/4906977/how-can-i-access-environment-variables-in-python
# https://www.geeksforgeeks.org/python-check-if-list-empty-not/
# https://stackoverflow.com/questions/4033723/how-do-i-access-command-line-arguments