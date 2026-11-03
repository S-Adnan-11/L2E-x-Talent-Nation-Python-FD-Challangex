def integer_to_roman(number):
    if not isinstance(number, int) or not 1 <= number <= 3999:
        return ""
    pairs = [(1000, "M"), (900, "CM"), (500, "D"), (400, "CD"),
             (100, "C"), (90, "XC"), (50, "L"), (40, "XL"),
             (10, "X"), (9, "IX"), (5, "V"), (4, "IV"), (1, "I")]
    roman = ""
    i = 0
    while number > 0:
        value, symbol = pairs[i]
        if number >= value:
            roman += symbol
            number -= value
        else:
            i += 1
    return roman


def roman_to_integer(roman):
    # week 7's look-ahead, wrapped for the round trips 😼
    values = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
    roman = roman.upper()
    if roman == "":
        raise ValueError("Roman numeral cannot be empty.")
    total = 0
    i = 0
    while i < len(roman):
        if roman[i] not in values:
            raise ValueError("Unknown Roman symbol.")
        current = values[roman[i]]
        if i + 1 < len(roman):
            if roman[i + 1] not in values:
                raise ValueError("Unknown Roman symbol.")
            if current < values[roman[i + 1]]:
                total -= current
            else:
                total += current
        else:
            total += current
        i += 1
    return total


if __name__ == "__main__":
    for number in (3, 58, 1994, 3999, 1, 0, 4000):
        print(number, "→", repr(integer_to_roman(number)))
    for number in range(1, 4000):
        if roman_to_integer(integer_to_roman(number)) != number:
            print("First failure:", number)
            break
    else:
        print("All round trips passed")
