num = int(input("Enter a five-digit integer: "))
for _ in range(5):
    digit = num % 10
    print(digit, end=' ')
    num //= 10