from math import remainder
from random import choice
def calculate(firstnum, operator,secondnum):
    if operator == '+':
        sum = firstnum + secondnum
        return sum
    elif operator == '*':
        multiply = firstnum * secondnum
        return multiply
    elif operator == '-':
        subtract = firstnum - secondnum
        return subtract
    elif operator == '/':
        divide = firstnum / secondnum
        return divide
    elif operator == '%':
        remainder = firstnum % secondnum
        return remainder
    else :
        return "invalid value"
print("welcome to our calculator".upper())
print("[1]addition\n[2]multiplication\n[3]subtraction\n[4]divide\n[5]reminder".title())
choose = input("enter your choice")
to_int = int(choose)
if to_int == 1:
    print("welcome to add wizard".title())
    num = input("enter first NO. ".title())
    to_int = int(num)
    num2 = input("Enter second NO. ".title())
    to_integer = int(num2)
    print(f"the sum of your numbers is {calculate(to_int, '+',to_integer)}")
    
    


