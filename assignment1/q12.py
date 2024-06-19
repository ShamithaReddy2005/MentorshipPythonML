# Write a python program that calculates the sum of the digits of a given number.

sum=0
num=int(input("enter the number"))
while (num>0) :
    sum+=num%10
    num=num//10
print (sum)
