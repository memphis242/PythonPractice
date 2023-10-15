import sys, os, fnmatch, re

def find( pattern, path ):
   result = []
   regex_obj = re.compile(pattern)
   for root, dirs, files in os.walk(path):
      for name in files:
         # print( name )
         if regex_obj.match(name):
            result.append(os.path.join(root, name))
      break    # Don't want to recurse into subfolders
   return result

#########################################################################
# Obtain the file pattern to search for from command-line arguments
#########################################################################
pattern_to_search = sys.argv[1]
if not pattern_to_search:
   print('No pattern specified!')
# pattern_to_search = '*gcc*'


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
# Apparently a single-line method of the below sublist iteration is: item for sublist in list_of_matches for item in sublist
for sublist in list_of_matches:
   for item in sublist:
      print(item)



# RESOURCES USED
# https://stackoverflow.com/questions/1724693/find-a-file-in-python
# https://docs.python.org/3/library/os.html#files-and-directories
# https://stackoverflow.com/questions/4117588/non-recursive-os-walk
# https://stackoverflow.com/questions/4906977/how-can-i-access-environment-variables-in-python
# https://www.geeksforgeeks.org/python-check-if-list-empty-not/
# https://stackoverflow.com/questions/4033723/how-do-i-access-command-line-arguments
# https://stackoverflow.com/questions/952914/how-do-i-make-a-flat-list-out-of-a-list-of-lists
# https://docs.python.org/3/library/fnmatch.html
# https://docs.python.org/3/library/re.html#functions