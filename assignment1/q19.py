# Write a python program that removes all punctuation from a given string.
punctuation = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
string = str(input("Enter a sentence "))
result = ""
for char in string:
    if char not in punctuation:
        result += char
print(f'Original: {string}')
print(f'Without punctuation: {result}')