def menu():
    while True:
        print("\nNOKIA MENU")
        print("1. Messages")
        print("2. Call Register")
        print("3. Profiles")
        print("4. Settings")
        print("5. Games")
        print("6. Calculator")
        print("7. Reminders")
        print("8. Clock")
        print("9. Tones")
        print("10. Services")
        print("0. Exit")

        choice = input("Choose option: ")

        match choice:
            case "1":
                messages()
            case "2":
                print("Call Register opened")
            case "3":
                print("Profiles opened")
            case "4":
                print("Settings opened")
            case "5":
                print("Games opened")
            case "6":
                print("Calculator opened")
            case "7":
                print("Reminders opened")
            case "8":
                print("Clock opened")
            case "9":
                print("Tones opened")
            case "10":
                print("Services opened")
            case "0":
                print("Exiting...")
                break
            case _:
                print("Invalid choice")


def messages():
    while True:
        print("\nMESSAGES MENU")
        print("1. Write Message")
        print("2. Inbox")
        print("3. Outbox")
        print("4. Templates")
        print("0. Back")

        choice = input("Choose option: ")

        match choice:
            case "1":
                print("Write Message selected")
            case "2":
                print("Inbox opened")
            case "3":
                print("Outbox opened")
            case "4":
                print("Templates opened")
            case "0":
                break
            case _:
                print("Invalid choice")


menu()