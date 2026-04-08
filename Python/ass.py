target = int(input("Enter the target sum: "))
total = int(input("Enter a number: "))

if total < target:
    total += int(input("Enter another number: "))

if total < target:
    total += int(input("Enter another number: "))

if total < target:
    total += int(input("Enter another number: "))

if total >= target:
    print("Done! The sum has reached or exceeded the target.")
