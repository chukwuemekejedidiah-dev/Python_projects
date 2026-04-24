def stringChecker():
    userInput = input("Enter a string: ")
    letters = []
    for char in userInput:
        if ('a' <= char <= 'z') or ('A' <= char <= 'Z'):
            letters.append(char)
    print("String found:", ''.join(letters))
    print("The number of string is: ", len(letters))

stringChecker()