def two_sumx(numsx, targetx):
    seenx = {}
    for indexx, numberx in enumerate(numsx):
        neededx = targetx - numberx
        # Check first, save after. One number can't pair with its own index 😹
        if neededx in seenx:
            return [seenx[neededx], indexx]
        if numberx not in seenx:
            seenx[numberx] = indexx
    return []


if __name__ == "__main__":
    try:
        numsx = [int(bitx) for bitx in input("Whole numbers, separated by spaces: ").split()]
        targetx = int(input("Target: "))
        print(two_sumx(numsx, targetx))
    except ValueError:
        print("Use whole numbers only.")
