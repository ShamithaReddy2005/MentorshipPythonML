# Write a python program that calculates the factorial of a given number.
value = int(input("Enter any number "))
factorial = 1
while(value>1):
    factorial = factorial*value
    value = value-1
print(factorial)