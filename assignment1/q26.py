# Write a program in python that checks if a string starts with a given prefix or ends with a given suffix.
prefix = input("Enter prefix to check ")
suffix = input("Enter suffix to check ")
string = input("Enter a string ")
if(string[1] == prefix):
    print("The string starts with the given prefix")
else:
    print("The string doesnot start with the given prefix")
if(string[-1] == suffix):
    print("The string ends with the given suffix")
else:
    print("The string doesnot end with the given suffix")