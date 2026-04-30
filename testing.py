balance = 1000
pin = 159234
user_name = "Admin"
password = "Admin123"

register_user()
login_user()

def main_menu():
    print("""
                1. Register
                2. Login
                3. Deposit
                4. Withdraw
                5. Check Balance
                6. Transfer
                7. Change PIN
                8. Transaction History
                9. Exit
                """)
    choice = int(input("Enter your choice: "))

    if choice == 1:
        register_user()

    elif choice == 2:
        serIndex = loginUser()
                break;
            case 3:
                if (userIndex != -1) {
                    deposit(userIndex);
                } else {
                    printf("Please login first.\n");
                }
                break;
            case 4:
                if (userIndex != -1) {
                    withdraw(userIndex);
                } else {
                    printf("Please login first.\n");
                }
                break;
            case 5:
                if (userIndex != -1) {
                    checkBalance(userIndex);
                } else {
                    printf("Please login first.\n");
                }
                break;
            case 6:
                if (userIndex != -1) {
                    transfer(userIndex);
                } else {
                    printf("Please login first.\n");
                }
                break;
            case 7:
                if (userIndex != -1) {
                    changePin(userIndex);
                } else {
                    printf("Please login first.\n");
                }
                break;
            case 8:
                if (userIndex != -1) {
                    transactionHistory(userIndex);
                } else {
                    printf("Please login first.\n");
                }
                break;
            case 9:
                printf("Thank you for using the ATM. Goodbye!\n");
                exit(0);
            default:
                printf("Invalid choice. Please try again.\n");
        }
    }

    return 0;
}