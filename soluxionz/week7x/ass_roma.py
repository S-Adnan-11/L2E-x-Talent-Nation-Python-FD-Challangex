values = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}

roman = input("Enter a Roman numeral: ").upper()

valid = True
for character in roman:
    if character not in values:
        valid = False

if not valid or roman == "":
    print("Invalid Roman numeral")
else:
    total = 0
    i = 0
    while i < len(roman):
        current = values[roman[i]]
        
        if i + 1 < len(roman) and current < values[roman[i + 1]]:
            total -= current
        else:
            total += current
        i += 1
    print(total)
