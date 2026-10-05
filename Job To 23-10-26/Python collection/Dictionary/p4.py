# Count frequency of characters using Dictionary.

test_string = "hello world"

string ={}

for i in test_string:
    if i in string:
        string[i] +=1
    else:
        string[i] = 1

print(string)