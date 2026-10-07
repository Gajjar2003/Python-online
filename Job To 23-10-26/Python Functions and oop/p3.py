# Write a function to find the largest of three numbers.


def largest_number(a,b,c):
     if a > b and a > c:
          return a
     elif b >c and b > a:
          return b
     else:
          return c

print(largest_number(100,210,300))