# Pattern 1
for i in range(1, 11):
    for j in range(i):
        print('*', end='')
    print()

print()

# Pattern 2
for i in range(10, 0, -1):
    for j in range(i):
        print('*', end='')
    print()

print()

# Pattern 3
for i in range(1, 11):
    for j in range(10-i):
        print(' ', end='')
    for j in range(i):
        print('*', end='')
    print()

print()

# Pattern 4
for i in range(10, 0, -1):
    for j in range(10-i):
        print(' ', end='')
    for j in range(i):
        print('*', end='')
    print()