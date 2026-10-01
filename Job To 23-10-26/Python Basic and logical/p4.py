# Write a program to find the largest of three numbers.


a = int(input("Enter first number:"))
b = int(input("Enter second number : "))
c = int(input("enter third number : "))

if a >b and a  >c :
  print("The largest number is ", a)
elif b > a and b > c :
  print("The largest number is ", b)
else : 
  print("The largest number is ", c)
