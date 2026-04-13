while True:
    answer = input("Have you had this problem before (1 for yes, 2 for no)? ")
    if answer == '1':
        print("Well, you have it again.")
        break
    elif answer == '2':
        print("Well, you have it now.")
        break
    else:
        print("Invalid input. Please enter 1 for yes or 2 for no.")