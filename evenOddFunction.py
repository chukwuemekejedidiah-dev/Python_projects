number = int( input("Enter a number: "))


def evenOrOdd(number):

    for index in range(1, number + 1):
        if index % 2 == 0:
            print(f"{index} is even")
        else:
            print(f"{index} is odd")


evenOrOdd(number)
