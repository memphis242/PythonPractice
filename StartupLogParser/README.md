# StartupLogParser
This repository holds the script that can be used to parse a CANsniff log that includes the messages involved in the STARTUP_LOG JD Console command I made for the eCTL TCU M50 and generate useful .csv files from the log data.

# Purpose
The goal is to make it as easy as possible to get startup data that might be difficult to thoroughly capture from our normal CAN tools (e.g., VSpy, MEP, etc.). One of the steps involved is parsing through the CANSniff file and generating a .csv file of the data in the log. This repo aims to accomplish that.

# How To Use
Simply invoke the Python script with the path to the file as a command-line argument.

## Tools Required:
* Python3+
* If you have any other python projects, it may be preferable to work on this repo from within a virtual environment. The simplest way to do that is using the python built-in `venv` tool:  
  * In a terminal window, run `python -m venv <name_of_folder_that_stores_virtual_environment>` where the folder is typically called `.venv`.  
  * Then basically run the activate script to "activate" the virtual environment in your current terminal session. To do that:  
    * For **Windows**: `. <venv_folder>\Scripts\active` (the '.' is intentional and is a command)  
    * For **POSIX-based** OS's (like UNIX): `source <venv_folder>/bin/activate`  
    * For **Ubuntu**: `. <venv_folder>/bin/activate` 
* To install the python dependencies, run: `pip install -r requirements.txt`. 

# Structure of Repository
TODO

