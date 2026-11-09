# Base n=0; //10 removes one digit each call.
def digit_sum(n):
    if not isinstance(n, int) or n < 0:
        raise ValueError("Use a non-negative integer.")
    if n == 0:
        return 0
    return n % 10 + digit_sum(n // 10)


# Base empty text; recurse on everything after the first character.
def reverse_text(text):
    if text == "":
        return ""
    return reverse_text(text[1:]) + text[0]


# Base empty text; count the first character, then shorten the text by one.
def count_char(text, ch):
    if len(ch) != 1:
        raise ValueError("ch must be one character.")
    if text == "":
        return 0
    return (1 if text[0] == ch else 0) + count_char(text[1:], ch)


# Base exp=0 gives 1; exp decreases by one each call.
def power(base, exp):
    if not isinstance(exp, int) or exp < 0:
        raise ValueError("Exponent must be a non-negative integer.")
    if exp == 0:
        return 1
    return base * power(base, exp - 1)


# Base exp=0; halve exp: 1000 needs 11 calls, versus power's 1001 (stack limit 😭).
def power_fast(base, exp):
    if not isinstance(exp, int) or exp < 0:
        raise ValueError("Exponent must be a non-negative integer.")
    if exp == 0:
        return 1
    half = power_fast(base, exp // 2)
    result = half * half
    if exp % 2:
        result *= base
    return result


if __name__ == "__main__":
    for n in (1234, 0, 7, 90009):
        print("Digit sum:", n, "→", digit_sum(n))
    for text in ("abc", "", "z", "ab ba"):
        print("Reverse:", repr(text), "→", repr(reverse_text(text)))
    for text, ch in (("banana", "a"), ("", "a"), ("aaaa", "a"), ("abc", "z")):
        print("Count:", repr(text), ch, "→", count_char(text, ch))
    for base, exp in ((2, 10), (5, 0), (-2, 3), (0, 4), (3, 8)):
        print("Power:", base, exp, "→", power(base, exp),
              "Fast match:", power(base, exp) == power_fast(base, exp))
    print("Fast power, exponent 1000:", power_fast(2, 1000))
