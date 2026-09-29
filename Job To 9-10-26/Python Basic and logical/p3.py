# Write a program to find the largest of two numbers.

num1 = int(input("Enter first number: "))
num2 = int(input("Enter seond number : "))

if  num1 >  num2:
  print("The largest number is ", num1)
elif num1 == num2:
  print("Both numbers are equal")
else:
  print("The largest number is ", num2)