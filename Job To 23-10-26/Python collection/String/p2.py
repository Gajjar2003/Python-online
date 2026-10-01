# Check whether a string is palindrome.

name = input("Enter Your name: ")

if name == name[::-1]:
    print(" palindrome.")
else:
    print(" no palindrome.")
