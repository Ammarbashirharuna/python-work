from datetime import date
from os import name
print("=================================")
print("WELCOME TO OUR PYTHON CALCULATOR")
print("=================================")
#addition function
def Add_function(first_number,second_number):
    numbers = first_number + second_number
    return numbers
#subtract function
def subtract_function(first_number,second_number):
    numbers = first_number - second_number
    return numbers
def multiply_function(firs_number,second_number):
    numbers = firs_number  * second_number
    return numbers


name = input("Your name Please!")
print("(1)Add\n(2)Subtract\n(3)multiply")
choice = input("Enter Your Choice")
number = int(choice)
if number == 1 :
    print("Wecome to Add Wizerd",name)
    first_number = input("Enter First NO ")
    to_int = int(first_number)
    second_number = input("Enter Second NO ")
    to_inte = int(second_number)
    total = Add_function(to_int,to_inte)
    print(f"the sum of your numbers is {total}")
elif number == 2 :
    print("Welcome to subtract wizard",name)
    first_number = input("Enter First NO ")
    to_int = int(first_number)
    second_number = input("Enter Second NO ")
    to_integer = int(second_number)
    total = subtract_function(to_int,to_integer)
    print(f"The Subtract of Your Numbers is {total}.")
elif number == 3 :
    print("Welcome to Subtract Wizard",name)
    first_number = input("Enter First NO ")
    to_int = int(first_number)
    second_number = input("Enter Second NO ")
    to_integer = int(second_number)
    total = multiply_function(to_int,to_integer)
    print(f"The multiply of Your Numbers is {total}.")






