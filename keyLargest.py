numbers = { "three": 35,"one": 15,"five": 55,"two": 25,"four": 45 }

largest_value = numbers["three"]

for key in numbers:
    if numbers[key] > largest_value:
        largest_value = numbers[key]

print("The largest value in this dictionary is ", largest_value)