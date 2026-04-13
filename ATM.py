


def access_atm():
  balance = 50000
  print("Welcome to ACCESS Bank ATM")
  
  while True    :
    print("\n1. Check Balance")
    print("2. Withdraw")
    print("3. Deposit")
    print("4. Exit")
    
    choice = input("Enter your choice: ")
    
    match choice:
      case '1':
        print(f"Your balance is ₦{balance}")
      case '2':
        amount = int(input("Enter amount to withdraw: "))
        if amount > balance:
          print("insufficient funds")
        elif amount > 50000:
          print("transaction limit exceeded")
        else:
          balance -= amount
          print(f"Withdrawal successful. New balance is ₦{balance}")
      case '3':
        amount = int(input("Enter amount to deposit: "))
        balance += amount
        print(f"Deposit successful. New balance is ₦{balance}")
      case '4':
        print("Thank you for using ACCESS Bank ATM")
        break
      case _:
        print("Invalid choice. Try again.")

access_atm()




