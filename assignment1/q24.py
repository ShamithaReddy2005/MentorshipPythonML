# Write a program that acts as a simple calculator. It should take two numbers and an operator (+, -, *, /) as input and print the result.
operator = input("Enter the mathematical operator you want to perform ")
value1 = int(input("Enter first value "))
value2 = int(input("Enter second value "))
if(operator == '+'):
    result = value1 + value2
    print(result)
elif(operator == '-'):
    result = value1 - value2
    print(result)
elif(operator == '*'):
    result = value1 * value2
    print(result)
elif(operator == '/'):
    result = value1 / value2
    print(result)