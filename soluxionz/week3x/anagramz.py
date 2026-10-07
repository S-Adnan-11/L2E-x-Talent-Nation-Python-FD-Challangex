#makes no sense obviously!
#turn around, turn around again, what th' ***, I'm facing the same direction
#don't turn around, don't turn around again, what th' ***, I'm facing the same direction

def character_countx(wordx):
    lettersx = {}
    for charx in wordx.lower():
        lettersx[charx] = lettersx.get(charx, 0) + 1
    return lettersx


def anagram_checkx(firstx, secondx):
    # Same letters isn't enough; the number of each letter has to match too.
    return character_countx(firstx) == character_countx(secondx)


if __name__ == "__main__":
    firstx = input("Word 1: ")
    secondx = input("Word 2: ")
    print("Anagram" if anagram_checkx(firstx, secondx) else "Not an anagram")
