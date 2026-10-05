# /Find unique elements from two Lists.

l1 = [1,2,3,4,5,6]
l2 = [4,5,6,7,8,9]

s1 = set(l1)
s2 = set(l2)

s3 = s1 ^ s2
print(s3)

