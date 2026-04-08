number = int(input("Enter the number of terms: "))
previous = 0
current = 1
sum = 0

for _ in range(number):
    sum += current
    next = previous + current
    previous = current
    current = next

print(sum)