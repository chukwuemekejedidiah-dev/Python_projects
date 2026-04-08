principal = float(input("Enter the principal amount: "))
interest_rate = 7
for year in range(1, 31):
    amount = principal * (1 + (interest_rate / 100)) ** year
    print(f"Year {year} is equal to {amount:.2f}")