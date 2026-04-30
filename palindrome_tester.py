def is_palindrome(text):
    normalized = ""
    for character in text:
        code = ord(character)
        if 65 <= code <= 90:
            code += 32
        if (97 <= code <= 122) or (48 <= code <= 57):
            normalized += chr(code)

    stack = []
    for character in normalized:
        stack.append(character)

    for character in normalized:
        top = stack[-1]
        stack = stack[:-1]
        if character != top:
            return False
    return True


print(is_palindrome("Radar"))
print(is_palindrome("Hello"))
