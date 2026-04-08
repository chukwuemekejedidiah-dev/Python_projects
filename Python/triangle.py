triangle_size = 5
for row in range(triangle_size):
    spaces = " " * (triangle_size - row - 1)
    asterisks = "*" * (2 * row + 1)
    print(spaces + asterisks)