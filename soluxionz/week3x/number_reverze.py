def number_reversex(numberx):
    signx = -1 if numberx < 0 else 1
    numberx *= signx
    reversedx = 0
    while numberx > 0:
        # Peel one digit off, then stick it onto the new number. Maths only 😹
        reversedx = reversedx * 10 + numberx % 10
        numberx //= 10
    return signx * reversedx


if __name__ == "__main__":
    try:
        numberx = int(input("Whole number: "))
        print(number_reversex(numberx))
    except ValueError:
        print("Use a whole number.")
