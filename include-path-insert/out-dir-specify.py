#################### ---IMPORTS--- #################### 
from typing import Tuple, List
import sys
import time
from datetime import timedelta
import math

#################### --CONSTANTS-- #################### 
# TODO: Update to be relative path and configure debugger's working directory to here so you can debug with file inputs...
TEST_INPUT = 'C:\git\quickScripts\PythonPractice\include-path-insert\EIC_MessageGateway_UT.vcxproj'
XML_ELEMENT_TO_FIND = '<LinkIncremental>'
OUT_DIR_ELEMENT_TO_ADD = '\t\t<OutDir>Builds\$(Configuration)\$(Platform)\</OutDir>'
INT_DIR_ELEMENT_TO_ADD = '\n\t\t<IntDir>Builds\Temp\$(Configuration)\$(Platform)\</IntDir>\n'

#################### --FUNCTIONS-- #################### 


#################### ----MAIN----- #################### 

# program_start_time = time.time()

if len(sys.argv) < 2:
   file_to_search = TEST_INPUT
   # file_to_search = SUB_PUZZLE_INPUT
else:
   file_to_search = sys.argv[1]

print(f'Specifying Output and Intermediate directories for project file: {file_to_search}')

with open(file_to_search, 'r') as file_input:
   file_input_lines = file_input.readlines()

ready_to_add = False
add_completed = False
with open(file_to_search, 'w') as replacement_file:
   for line in file_input_lines:
      # TODO: If file _already_ contains a specified OutDir or IntDir, need to replace-in-place, not add!
      if (XML_ELEMENT_TO_FIND in line):
         replacement_file.write(line)
         replacement_file.write(OUT_DIR_ELEMENT_TO_ADD)
         replacement_file.write(INT_DIR_ELEMENT_TO_ADD)
      else:
         replacement_file.write(line)



# program_end_time = time.time()
# total_program_time = program_end_time - program_start_time
# total_program_time_hh_mm_ss = str(timedelta( seconds=total_program_time ))
# hh_mm_ss = total_program_time_hh_mm_ss.split(':')
# print(f'\nTotal Program Execution Time: {hh_mm_ss[0]}h {hh_mm_ss[1]}m {hh_mm_ss[2]}s')