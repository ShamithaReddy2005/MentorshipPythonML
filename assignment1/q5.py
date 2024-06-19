# Write a program that takes a string input from the user and writes it to a text file.
value = str(input("Enter a string "))
samplefile = open("C:/Users/shami/OneDrive/Desktop/MentorshipPythonML/printfromq5.txt", 'w')
print(value , file=samplefile)