correct_numbers = [1, 2, 3]  

def add(a, b):
    return a + b   

def test_add(func):
    result = func(9, 1)
    print("Test result:", result)


a = int(input("Enter your first number: "))
b = int(input("Enter your second number: "))


print("Sum:", add(a, b))

test_add(add)
