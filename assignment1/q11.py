# Write a python program that generates the first n numbers in the Fibonacci sequence.
value = int(input("Enter a number "))
num1 = 0
num2 = 1
temp = num1
num = []
while(value>0):
    num.append(num1)
    num1 = num2
    num2 = temp+num2
    temp = num1
    value = value-1
print(num)