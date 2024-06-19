#  Write a program that copies the contents of one text file to another.
readingfile = open("C:/Users/shami/OneDrive/Desktop/MentorshipPythonML/printfromq5.txt",'r')
content = readingfile.read()
# print(content)
writingfile = open("C:/Users/shami/OneDrive/Desktop/MentorshipPythonML/readfromq5filewriteinthis.txt", 'w')
print(content , file=writingfile)