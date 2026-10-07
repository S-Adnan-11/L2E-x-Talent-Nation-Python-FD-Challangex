def make_shifter(shift):
    def shift_charx(charx):
        if "a" <= charx <= "z":
            basex = ord("a")
        elif "A" <= charx <= "Z":
            basex = ord("A")
        else:
            return charx
        return chr(basex + (ord(charx) - basex + shift) % 26)

    # shift stays in this little closure, even after make_shifter returns 😼
    return shift_charx


def caesarx(textx, shiftx, modex):
    if modex not in ("encrypt", "decrypt"):
        raise ValueError("Mode must be encrypt or decrypt.")
    if modex == "decrypt":
        shiftx = -shiftx
    return "".join(map(make_shifter(shiftx), textx))


if __name__ == "__main__":
    modex = input("Encrypt or decrypt? ").strip().lower()
    textx = input("Message: ")
    try:
        shiftx = int(input("Shift: "))
        print(caesarx(textx, shiftx, modex))
    except ValueError as errorx:
        print(f"Check your mode/whole-number shift: {errorx}")
