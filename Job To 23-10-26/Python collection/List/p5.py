# Find duplicate elements in a list.  


numbers = [10, 20, 10, 30, 20, 40]

for i in numbers:
    if numbers.count(i) > 1:
        print(i)