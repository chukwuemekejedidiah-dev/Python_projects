numbers = { "d": 40, "b": 20, "e": 50, "a": 10, "c": 30 }


for key in numbers:
    smallest_key = key
    smallest_value = numbers[key]
    break

for key in numbers:
    if numbers[key] < smallest_value:
        smallest_value = numbers[key]
        smallest_key = key

print("The key associated with the smallest value is", smallest_key)
