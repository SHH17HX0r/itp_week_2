# ITP Week 2 Day 3 Exercise

# Write a basic calculator using the input function to complete the following tasks.  Be sure to call your functions at the end, using the correct arguments.

import math

# Easy:
#     - A function that subtracts one integer from another
#     - A function that multiplies three integers
#     - A function that adds four integers


def Sub_2nums(x, y):
    return x-y


def Multi_3nums(x, y, z):
    return x * y * z * z


def Add_4nums(w, x, y, z):
    return w + x + y + z

# Medium:
#     - Create a calculator function using THREE input parameters (two float, one string[hint: it will be a math symbol]) to allow the user to add, substract, multiply and divide.


def calc(a, b, c=str):
    if c == '+':
        return a + b
    elif c == '-':
        return a - b
    elif c == '*':
        return a * b
    elif c == '/':
        return a/b
    else:
        print('An improper operand was passed. Please use +, -, *, or /')


print(calc(2, 5, '/'))

# Hard:
#     - You're at a restaurant with some friends and the server didn't split up the check.  Create a function that takes a bill amount, multiplies it by a global variable called tax_rate, adds the tax, and then divides the total bill by the number of people input by the user.  BONUS:  Include an option for adding tip through either a percentage amount assigned to a global variable, or through a specific amount input by the user.  You may use the math module from the Python standard library.
