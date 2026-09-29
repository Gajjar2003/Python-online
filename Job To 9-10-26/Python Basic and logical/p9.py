# Write a program to print the multiplication table of a number.

# num = int(input("Enter your number is : "))

# for i in range(1,11):
#   print(num , "X" ,i , " =" ,num*i)


x = 10
y = 20

print(x > y)
print(x < y)



num = int(input("Enter number: "))

reverse = 0
original = num

while num > 0:
    digit = num % 10
    reverse = reverse * 10 + digit
    num = num // 10

if original == reverse:
    print("Palindrome")
else:
    print("Not Palindrome")



n = int(input("Enter number: "))

reverse = 0

while n > 0:
    digit = n % 10
    reverse = reverse * 10 + digit
    n = n // 10

print("Reverse =", reverse)