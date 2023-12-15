#################### ---IMPORTS--- #################### 
from typing import Tuple, List
import sys
import time
from datetime import timedelta
import math

#################### --CONSTANTS-- #################### 
# TODO: Update to be relative path and configure debugger's working directory to here so you can debug with file inputs...
TEST_INPUT = 'EIC_MessageGateway_UT.vcxproj'
INCLUDE_PATH_TO_APPEND = '..\\..\\..\\node_modules\\@deere-embedded\\construction-backhoe.ett\\Stubs\\Core\\;'
XML_ELEMENT_TO_FIND = '<AdditionalIncludeDirectories>'

#################### --FUNCTIONS-- #################### 


#################### ----MAIN----- #################### 

program_start_time = time.time()

if len(sys.argv) < 2:
   file_to_search = TEST_INPUT
   # file_to_search = SUB_PUZZLE_INPUT
else:
   file_to_search = sys.argv[1]

with open(file_to_search, 'r') as file_input:
   file_input_lines = file_input.readlines()

with open(file_to_search, 'w') as replacement_file:
   for line in file_input_lines:
      if XML_ELEMENT_TO_FIND in line:
         # Split the line's string on ';', then add at the index _prior_ to the last element the new include path
         split_line = line.split(';')
         split_line.insert(-1, INCLUDE_PATH_TO_APPEND)
         new_line = ''.join(split_line)
         replacement_file.write(new_line)
      else:
         replacement_file.write(line)

program_end_time = time.time()
total_program_time = program_end_time - program_start_time
total_program_time_hh_mm_ss = str(timedelta( seconds=total_program_time ))
hh_mm_ss = total_program_time_hh_mm_ss.split(':')
print(f'\nTotal Program Execution Time: {hh_mm_ss[0]}h {hh_mm_ss[1]}m {hh_mm_ss[2]}s')