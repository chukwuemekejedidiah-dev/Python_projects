max1 = max2 = float('-inf')
for i in range(10):
    num = float(input(f"Enter number {i+1}: "))
    if num > max1:
        max2 = max1
        max1 = num
    elif num > max2:
        max2 = num

print(f"Largest number: {max1}")
print(f"Second largest number: {max2}")