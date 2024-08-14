from datetime import date
#program to calculate the age
print("Todays date is :", (date.today()))
name = input("Enter Your name")
print("welcome to Age Calculator",name)
Birth_year = input("Enter your birth Year")
#converting string to a number
by = int(Birth_year)
years =  int(2024 - by)
print(f"{name}  you are  {years} Years  Old")

