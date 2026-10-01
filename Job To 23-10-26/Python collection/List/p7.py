# Separate even and odd numbers.  

numbers = [1, 2, 3, 4, 5, 6]

even = []
odd = []

for i in numbers:
    if i % 2 == 0:
        even.append(i)
    else:
        odd.append(i)

print("Even:", even)
print("Odd:", odd)