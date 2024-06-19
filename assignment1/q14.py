# Write a program that reads multiple lines of input from the user until they enter an empty line, then prints all the lines.

lines = []
while True:
    line = input("Enter a line (or press Enter to finish): ")
    if line == "":
        break
    lines.append(line)

print("You entered:")
for i in lines:
    print(i)