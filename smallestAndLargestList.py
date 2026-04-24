numbers = [20, 15, 12, 5, 99]

def find_max(numbers):
    max = numbers[0]
    for num in numbers:
        if num > max:
            max = num
    return max

def find_min(numbers):
    min = numbers[0]
    for num in numbers:
        if num < min:
            min = num
    return min

print("Maximum:", find_max(numbers))
print("Minimum:", find_min(numbers))
