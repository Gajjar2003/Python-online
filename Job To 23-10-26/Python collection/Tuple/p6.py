# Find duplicate elements.

t = (1,2,3,4,5,6,1,2,3,4,5,6)

for i in t :
  if t.count(i) > 1:
    print(i)