def digitChecker():
    userInput = input("Enter a string: ")
    digits = []
    for char in userInput:
        if '0' <= char <= '9':
            digits.append(char)
    print("Digits found:", ''.join(digits))
    print("The number of digits is:", len(digits))

digitChecker()