# Write a function to find the factorial of a number.


def factorial(num):
    fact = 1
    
    for i in range(1,num+1):
        fact = fact*i
    print(fact)


factorial(5)