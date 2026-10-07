# Write a function to check whether a string is palindrome.

def palindrome(text):
    if text == text[::-1]:
        return True
    else:
        return False


text = input("Enter string: ")

if palindrome(text):
    print("Palindrome")
else:
    print("Not Palindrome")