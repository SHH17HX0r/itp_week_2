# ITP Week 2 Day 3 Exercise

# Write a basic calculator using the input function to complete the following tasks.  Be sure to call your functions at the end, using the correct arguments.

import math

# Easy:
#     - A function that subtracts one integer from another
#     - A function that multiplies three integers
#     - A function that adds four integers


# def Sub_2nums(x, y):
#     return x-y


# def Multi_3nums(x, y, z):
#     return x * y * z * z


# def Add_4nums(w, x, y, z):
#     return w + x + y + z

# # Medium:
# #     - Create a calculator function using THREE input parameters (two float, one string[hint: it will be a math symbol]) to allow the user to add, substract, multiply and divide.


# def calc(a, b, c=str):
#     if c == '+':
#         return a + b
#     elif c == '-':
#         return a - b
#     elif c == '*':
#         return a * b
#     elif c == '/':
#         return a/b
#     else:
#         print('An improper operand was passed. Please use +, -, *, or /')


# print(calc(2, 5, '/'))

# Hard:
#     - You're at a restaurant with some friends and the server didn't split up the check.  Create a function that takes a bill amount, multiplies it by a global variable called tax_rate, adds the tax, and then divides the total bill by the number of people input by the user.  BONUS:  Include an option for adding tip through either a percentage amount assigned to a global variable, or through a specific amount input by the user.  You may use the math module from the Python standard library.


def calc_tax(tax_rate, meal_total):
    return tax_rate * meal_total


def calc_tip(meal_total):
    tip_amt = float(input(
        'please enter the percentage tip that you would like to leave. ie. 20 '))
    return (tip_amt / 100) * meal_total


def Split_Bill(meal_total, meal_tax, tip, num_customers):
    return (meal_total + meal_tax + tip) / num_customers


def main():

    tax_rate = .07      # Global Constant Tax

    meal_total = float(input('Meal total?  '))
    num_customers = int(input('How many customers to split the bill?  '))

    tot_tax = calc_tax(tax_rate, meal_total)
    tot_tip = calc_tip(meal_total)

    per_customer = Split_Bill(meal_total, tot_tax, tot_tip, num_customers)
    print('Each customer will need to pay $' + str(per_customer))


if __name__ == "__main__":
    main()
