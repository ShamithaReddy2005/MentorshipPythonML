def count_char_frequency(s):
    frequency = {}
    for char in s:
        if char in frequency:
            frequency[char] += 1
        else:
            frequency[char] = 1
    return frequency

s = input("Enter a string: ")
frequency = count_char_frequency(s)

print("Character frequencies:")
for char, count in frequency.items():
    print(f"{char}: {count}")
