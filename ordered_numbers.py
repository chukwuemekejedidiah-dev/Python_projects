import random

letters = []
for _ in range(20):
    letters.append(chr(random.randint(ord('a'), ord('f'))))

ascending = sorted(letters)
descending = sorted(letters, reverse=True)

unique = []
for ch in ascending:
    if ch not in unique:
        unique.append(ch)

print("Original:", letters)
print("Ascending:", ascending)
print("Descending:", descending)
print("Unique Ascending:", unique)



# for i in range(65, 91):
#     print(i, chr(i))

# chr() => from ASCII value to the character
# ord() => form character to ASCII value