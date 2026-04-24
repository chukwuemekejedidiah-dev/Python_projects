def add(numbers):
    total = 0
    for num in numbers:
        total += num
    return total

numbers = [10, 20, 30, 40, 50]

def sum_and_average(numbers):
    total = add(numbers)
    average = total / len(numbers)
    return total, average



total, avg = sum_and_average(numbers)

print("Sum:", total)
print("Average:", avg)
