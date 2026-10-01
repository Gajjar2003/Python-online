# Count vowels and consonants.


name = input("Enter Your name: ")

vowels = 0
copnsonants = 0

for i in name:
    if i in "aeiou":
        vowels +=1
    else:
        copnsonants +=1

print("Vowels: ", vowels)
print("Consonants: ", copnsonants)