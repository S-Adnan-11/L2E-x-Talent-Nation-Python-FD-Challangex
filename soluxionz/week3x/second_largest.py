def second_largestx(numsx):
    largestx = None
    runnerx = None
    for numberx in numsx:
        if largestx is None or numberx > largestx:
            runnerx = largestx
            largestx = numberx
        elif numberx != largestx and (runnerx is None or numberx > runnerx):
            runnerx = numberx
    # None means we never found two different numbers. Zero is a real answer.
    return runnerx


if __name__ == "__main__":
    try:
        numsx = [float(bitx) for bitx in input("Numbers, separated by spaces: ").split()]
        resultx = second_largestx(numsx)
        print("Need at least two unique numbers." if resultx is None else resultx)
    except ValueError:
        print("Use numbers only.")
