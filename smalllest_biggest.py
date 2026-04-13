numbers = []
for i in range(4):
    numbers.append(int(input(f"Enter integer {i+1}: ")))

total = 0
product = 1
smallest = largest = numbers[0]

for num in numbers:
    total += num
    product *= num
    if num < smallest:
        smallest = num
    if num > largest:
        largest = num

print(f"Sum: {total}")
print(f"Average: {total/4}")
print(f"Product: {product}")
print(f"Smallest: {smallest}")
print(f"Largest: {largest}")