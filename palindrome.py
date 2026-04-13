num = input("Enter a 5-digit number: ")

if len(num) == 5:
    if num[0] == num[4] and num[1] == num[3]:
        print("The number is a palindrome.")
    else:
        print("The number is not a palindrome.")
else:
    print("Only 5-digit numbers please.")