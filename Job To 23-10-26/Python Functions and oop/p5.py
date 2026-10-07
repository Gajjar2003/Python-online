# Write a function to check whether a number is prime.


def prime(num):
    for i in range(2, num):
        if num % i == 0:
            return False
    return True


num = int(input("Enter number: "))

if prime(num):
    print("Prime")
else:
    print("Not Prime")