numbers = [23, 65, 19, 90]

print("Before swap:", numbers)

for index in range(len(numbers)):
     swap = numbers[index]
     numbers[index] = numbers[2]
     numbers[2] = swap
       

print("After swap:", numbers)
