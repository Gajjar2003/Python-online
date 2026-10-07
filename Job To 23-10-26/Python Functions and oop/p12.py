# Write a function using `*args` to find the sum of numbers.  

def total(*args):
    sum = 0

    for i in args:
        sum += i

    return sum


print(total(10, 20, 30))