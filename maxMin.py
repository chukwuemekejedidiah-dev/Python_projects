my_numbers = []
for i in range(10):
    num = int(input(f"Enter a number {i+1}: "))
    my_numbers.append(num)

def maxNum(numbers):
    maxNumber = numbers[0]
    for num in numbers[1:10]:
        if num > maxNumber:
          maxNumber = num
    print("The maximum number is:", maxNumber)



def  minNum(numbers):
    minNumber = numbers[0]
    for num in numbers[1:10]:
        if num < minNumber: 
            minNumber = num
    print("The minimum number is:", minNumber)


maxNum(my_numbers)
minNum(my_numbers)