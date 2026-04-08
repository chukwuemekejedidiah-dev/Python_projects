length = 5

for outerLoop in range(1, 6):
    for innerLoop in range(1, outerLoop + 1):
        print(innerLoop, end=" ")
    print("\n", end = "")