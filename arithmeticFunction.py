import random
random.seed(32)

def generateNumbers():
    numbers = [random.randrange(1, 20) for _ in range(20)]
    print(numbers)
    return numbers

numbers = generateNumbers()

def findMaximum(nums):
    max_num = nums[0]
    for max in nums:
        if max > max_num:
            max_num = max
    return max_num

def findMinimum(nums):
    min_num = nums[0]
    for min in nums:
        if min < min_num:
            min_num = min
    return min_num

print("Maximum is:", findMaximum(numbers))
print("The minimum of the number is: ", findMinimum(numbers))