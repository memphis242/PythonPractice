# Environmental Variable Echo Output to CSV and Text
This Python script is meant to be a convenient way to get a `.txt` and `.csv` file version of what an echo of an environmental variable would produce as console output. The output is typically a single line with items in the list for the environmental variable separate by a single character, such as ':' or ';'. I'd rather have that separate be a newline so this is easier to read and search through.  

## Typical Use
### bash
1- `printenv PATH > <path_name_and_date>.txt`
1- `python EnvVarEcho_To_CSVandText.py <path_name_and_date>.txt [<separation character>]`
### Windows Command Prompt
Same thing but `echo %PATH%` instead of `printenv PATH`
