# Write a function to count vowels in a string.


def count_vowels(string):
    vowels = "aeiou"
    count  = 0

    for i in string:
        if i in vowels:
            count +=1

    return count

print(count_vowels("hello"))