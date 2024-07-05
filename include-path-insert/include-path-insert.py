#################### ---IMPORTS--- #################### 
from typing import Tuple, List
import sys
import time
from datetime import timedelta
import math

#################### --CONSTANTS-- #################### 
# TODO: Update to be relative path and configure debugger's working directory to here so you can debug with file inputs...
TEST_INPUT = 'C:\git\quickScripts\PythonPractice\include-path-insert\EIC_MessageGateway_UT.vcxproj'
INCLUDE_PATH_TO_APPEND = '..\\..\\..\\node_modules\\@deere-embedded\\construction-backhoe.ett\\Stubs\\Core\\'
XML_ELEMENT_TO_FIND = '<AdditionalIncludeDirectories>'
ELEMENT_TO_ADD = '\t\t<WindowsTargetPlatformVersion>10.0</WindowsTargetPlatformVersion>\n'
ELEMENT_TO_FIND_BEFORE_ELEMENT_ADD = 'RootNamespace'

#################### --FUNCTIONS-- #################### 


#################### ----MAIN----- #################### 

# program_start_time = time.time()

if len(sys.argv) < 2:
   file_to_search = TEST_INPUT
   # file_to_search = SUB_PUZZLE_INPUT
else:
   file_to_search = sys.argv[1]

print(f'Applying insertion to the file: {file_to_search}')

with open(file_to_search, 'r') as file_input:
   file_input_lines = file_input.readlines()

ready_to_add = False
add_completed = False
with open(file_to_search, 'w') as replacement_file:
   for line in file_input_lines:
      if ready_to_add == True:
         ready_to_add = False
         replacement_file.write(ELEMENT_TO_ADD)
         add_completed = True
      if add_completed == False and ELEMENT_TO_FIND_BEFORE_ELEMENT_ADD in line:
         replacement_file.write(line)
         ready_to_add = True
         continue

      if ELEMENT_TO_ADD in line:
         continue

      if (XML_ELEMENT_TO_FIND in line) and (INCLUDE_PATH_TO_APPEND not in line):
         # Split the line's string on ';', then add at the index _prior_ to the last element the new include path
         split_line = line.split(';')
         split_line.insert(-1, INCLUDE_PATH_TO_APPEND)
         new_line = ';'.join(split_line)
         replacement_file.write(new_line)
      else:
         replacement_file.write(line)



# program_end_time = time.time()
# total_program_time = program_end_time - program_start_time
# total_program_time_hh_mm_ss = str(timedelta( seconds=total_program_time ))
# hh_mm_ss = total_program_time_hh_mm_ss.split(':')
# print(f'\nTotal Program Execution Time: {hh_mm_ss[0]}h {hh_mm_ss[1]}m {hh_mm_ss[2]}s')


########## LINKS/REFERENCES I USED ##########
https://stackoverflow.com/questions/3437059/does-python-have-a-string-contains-substring-method
https://stackoverflow.com/questions/39086/search-and-replace-a-line-in-a-file-in-python
https://www.programiz.com/python-programming/file-operation?_sm_au_=iVVHfvpFSRD6FWtLL321jK0f1JH33#:~:text=In%20order%20to%20write%20into,()%20as%20a%20second%20argument.
https://www.w3schools.com/python/ref_string_split.asp
https://stackoverflow.com/questions/5618878/how-to-convert-list-to-string
https://www.geeksforgeeks.org/python-list-insert/
https://stackoverflow.com/questions/7866128/python-split-without-removing-the-delimiter
https://stackoverflow.com/questions/30898038/python-run-script-on-multiple-files
