num = int(input("Enter a number: "))
largest = smallest = num % 10
num = num // 10


while num > 0:   
    count = num % 10  
    if count > largest:   
        largest = count     
    elif count < smallest:   
        smallest = count    
    num = num // 10

print(f"Largest digit: {largest}")
print(f"Smallest digit: {smallest}")