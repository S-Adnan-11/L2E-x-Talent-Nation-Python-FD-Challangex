def caesarx(textx, shiftx, modex):
    if modex not in ("encrypt", "decrypt"):
        raise ValueError("Mode must be encrypt or decrypt.")
    if modex == "decrypt":
        shiftx = -shiftx

    resultx = ""
    for charx in textx:
        if "a" <= charx <= "z":
            basex = ord("a")
        elif "A" <= charx <= "Z":
            basex = ord("A")
        else:
            resultx += charx
            continue
        # % 26 brings z back round to a. Negative shifts wrap too 😼
        resultx += chr(basex + (ord(charx) - basex + shiftx) % 26)
    return resultx


if __name__ == "__main__":
    modex = input("Encrypt or decrypt? ").strip().lower()
    textx = input("Message: ")
    try:
        shiftx = int(input("Shift: "))
        print(caesarx(textx, shiftx, modex))
    except ValueError as errorx:
        print(f"Check your mode/whole-number shift: {errorx}")
