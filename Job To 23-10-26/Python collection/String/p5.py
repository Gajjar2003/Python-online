# Find duplicate characters in a string.


text = input("Enter string: ")

for char in text:
    if text.count(char) > 1:
        print(char)