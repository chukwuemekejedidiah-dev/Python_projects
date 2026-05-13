def character_counts_with_ascii():
    sentence = input("Enter a sentence: ").lower().replace(" ", "")

    counts = {}
    for code in range(ord('a'), ord('z') + 1):
        letter = chr(code)
        counts[letter] = sentence.count(letter)

    for letter in sorted(counts.keys()):
        if counts[letter] > 0:
            print(f"  {letter} {counts[letter]}")

character_counts_with_ascii()
