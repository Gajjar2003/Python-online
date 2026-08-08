num = [10,55,77,9,100,300,7,9,6]

lag = num[0]
for i in num:
    if  i>lag:
        lag = i
print("Largest number is:",lag)