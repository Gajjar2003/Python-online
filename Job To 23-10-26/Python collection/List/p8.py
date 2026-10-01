# Find maximum and minimum without using max() and min().

numbers = [10, 25, 5, 40, 15]

maximum = numbers[0]
minimum = numbers[0]

for i in numbers:
    if i > maximum:
        maximum = i

    if i < minimum:
        minimum = i

print("Maximum:", maximum)
print("Minimum:", minimum)