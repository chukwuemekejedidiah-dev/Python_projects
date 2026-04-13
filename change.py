price = float(input("Enter the purchase price (less than or equal to 1 dollar): "))
change = round((1 - price) * 100)

quarters = change // 25
change %= 25
dimes = change // 10
change %= 10
nickels = change // 5
pennies = change % 5

print("Your change is:", end=' ')
if quarters > 0:
    print(f"{quarters} quarter{'s' if quarters > 1 else ''}", end=' ')
if dimes > 0:
    print(f"{dimes} dime{'s' if dimes > 1 else ''}", end=' ')
if nickels > 0:
    print(f"{nickels} nickel{'s' if nickels > 1 else ''}", end=' ')
if pennies > 0:
    print(f"{pennies} penn{'ies' if pennies > 1 else 'y'}", end=' ')
print()