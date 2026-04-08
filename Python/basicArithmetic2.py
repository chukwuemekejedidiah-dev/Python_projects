number = float(input("Enter a number: "))
square = number ** 2
if number >= 100 and square >= 100:
    print("Both the number and its square are greater than or equal to 100.")
elif number < 100 and square < 100:
    print("Both the number and its square are less than 100.")
else: print("one is greater than or equal to 100 and the other is less than 100")