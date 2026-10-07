def two_sum(nums, target) -> list[int]:
    seenx = {}
    for indexx, numberx in enumerate(nums):
        neededx = target - numberx
        if neededx in seenx:
            return [seenx[neededx], indexx]
        if numberx not in seenx:
            seenx[numberx] = indexx
    return []


if __name__ == "__main__":
    try:
        numsx = [int(bitx) for bitx in input("Whole numbers, separated by spaces: ").split()]
        targetx = int(input("Target: "))
        print(two_sum(numsx, targetx))
    except ValueError:
        print("Use whole numbers only.")
