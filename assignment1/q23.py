# Write a program that converts temperature from Celsius to Fahrenheit and vice versa based on user input.
typeofconversion = input("Enter type of conversion ")
if(typeofconversion == 'c to f'):
    celsius = float(input("Enter temperature in celsius "))
    farenheit = (celsius * 9/5) + 32
    print(farenheit)
else : 
    farenheit = float(input("Enter temperature in farenheit "))
    celsius = (farenheit - 32) * 5/9
    print(celsius)