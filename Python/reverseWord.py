word = input("Enter a word: ")
reverse_word = ""
for i in range(len(word)):
  reverse_word += word[::-1]
print(f"{reverse_word} is the reverse of {word}")
if word == reverse_word:
  print(f"{reverse_word} is a palindrome")
else:
  print(f"{reverse_word} is not a palindrome")  