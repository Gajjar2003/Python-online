# Count the frequency of each character.  


text = input("Enter string: ")

for char in text:
    print(char, ":", text.count(char))


