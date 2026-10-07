def is_letter(ch):
    return ch.isalpha()


def is_palindrome(text):
    leftx = 0
    rightx = len(text) - 1
    while leftx < rightx:
        # Keep digits too; only spaces/punctuation get skipped.
        if not is_letter(text[leftx]) and not text[leftx].isnumeric():
            leftx += 1
        elif not is_letter(text[rightx]) and not text[rightx].isnumeric():
            rightx -= 1
        elif text[leftx].lower() != text[rightx].lower():
            return False
        else:
            leftx += 1
            rightx -= 1
    return True


def is_palindrome_recursive(text, left=0, right=None):
    if right is None:
        right = len(text) - 1
    if left >= right:
        return True
    if not is_letter(text[left]) and not text[left].isnumeric():
        return is_palindrome_recursive(text, left + 1, right)
    if not is_letter(text[right]) and not text[right].isnumeric():
        return is_palindrome_recursive(text, left, right - 1)
    if text[left].lower() != text[right].lower():
        return False
    return is_palindrome_recursive(text, left + 1, right - 1)


if __name__ == "__main__":
    textx = input("Sentence: ")
    print("Palindrome" if is_palindrome(textx) else "Not a palindrome")
    print("Recursive bonus:", is_palindrome_recursive(textx))
