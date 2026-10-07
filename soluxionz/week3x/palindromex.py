def palindrome_checkx(textx):
    leftx = 0
    rightx = len(textx) - 1

    while leftx < rightx:
        # The pointers dodge punctuation themselves. No cleaned/reversed copy 😼
        if not textx[leftx].isalnum():
            leftx += 1
        elif not textx[rightx].isalnum():
            rightx -= 1
        elif textx[leftx].lower() != textx[rightx].lower():
            return False
        else:
            leftx += 1
            rightx -= 1
    return True


if __name__ == "__main__":
    textx = input("Sentence: ")
    print("Palindrome" if palindrome_checkx(textx) else "Not a palindrome")
