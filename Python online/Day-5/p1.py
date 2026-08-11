text = "hello"

count = {}

for char in text:
    count[char] = count.get(char, 0) + 1

print(count)



nums = [1,2,4,1,5,7,9,1,2,3]

sum = []

for num in nums:
    if num not in sum:
        sum.append(num)
print(sum)