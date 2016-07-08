"""
calculator.py

Using our arithmetic.py file from Exercise02, create the
calculator program yourself in this file.
"""

from arithmetic import *


# # Your code goes here
# def check_string(input_string):
#     tokens = input_string.split(" ")
#     print tokens
#     try: 
#         tokens[1:].isdigit()
#         print "foo"

#     except:
#         print "Invalid Command"

# check_string("* 2 5")

def new_calculator():
    while True:
        input_string = raw_input("What would you like to calculate?     ")
        tokens = input_string.split(" ")
        
        if tokens[1].isdigit() and tokens[2].isdigit():
        
            tokens[1] = int(tokens[1])
            tokens[2] = int(tokens[2])        

            if tokens[0] == "q":
                break
       
            elif tokens[0] == "+":
                print add(tokens[1], tokens[2])

            elif tokens[0] == "-":
                print subtract(tokens[1], tokens[2])

            elif tokens[0] == "*":
                print multiply(tokens[1], tokens[2])

            elif tokens[0] == "/":
                print divide(tokens[1], tokens[2])

            elif tokens[0] == "**":
                print square(tokens[1])

            elif tokens[0] == "**3":
                print cube(tokens[1])

            elif tokens[0] == "pow":
                print power(tokens[1], tokens[2])

            elif tokens[0] == "%":
                print mod(tokens[1], tokens[2])

            else:
                print "Invalid Input"

        else:
            print "Invalid Calculation"      

new_calculator()