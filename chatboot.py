from os import name, system


name = input("enter your name\t\t".title())
system("cls")
print("welcome",name)
print("am here to help you".title())
conver = input("Enter prompt Here".upper())
if conver == "what is your name ":
    print("my name is neuron and i am large language model")
elif conver == "What is my name ":
    print("your name is")

