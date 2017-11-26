"""
This is where I put all relevant practice code from
Chapters 1 and 2 of Fundamentals of Python - From
First Programs Through Data Structures, Lambert 2010.
"""

#CHAPTER 1

# READING
#print 'How you doing.'
#currentState = input('Answer: ') --> INPUT FUNCTION CALLS EVAL(RAW_INPUT(...)), WHICH IN TURN EVALUATES THE EXPRESSION INSIDE, INCLUDING METHOD CALLS,
# AND DOES NOT UNDERSTAND STRINGS. IT IS ALIKE TO TYPING A COMMAND IN THE PYTHON SHELL.
#currentStateTwo = raw_input('Answer: ')
#print currentState
#print currentStateTwo

# EXERCISES
# 2
# name = raw_input('Name: ')
# address = raw_input('Address: ')
# telephoneNumber = raw_input('Telephone Number: ')
# print
# print 'Your Name: ' + name + '\n' + 'Your Address: ' + address + '\n' + 'Your Telephone Number: ' + telephoneNumber

#--------------------------------------------------

#CHAPTER 2

#READING
#Displaying single-quotations or double-quotations when printing
# print "'Hey there!' said Bob." + '\n' +\
#       '"Hey there!" said Bob.'
#NOTE THE '+\' ABOVE! It allows for multiple lines in the editor.
#There is also the method using ESCAPE SEQUENCES
# print '\'Hey there!\' said Bob.' + '\n' +\
#     '\"Hey there!\" said Bob.'

'''
Example MULTI-LINE BLOCK COMMENT - EY! IT WORKS! # still recommended.
'''

#Use of ord() and chr() to exemplify ASCII character literals in Python
print ord('A')
print chr(100)
print chr(ord('A') + 3)     #shifting A three places to the right
