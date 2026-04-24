userName = input("Enter username: ")
addStringNumber ?
def addstringNumber():
    words = 0
    number = 0
    
    for user in userName:     
        if user.isdigit():
            number += 1
        else:
            words += 1

    total_num = words + number
    print("The total of the strings and digits is:", total_num)

addstringNumber()
