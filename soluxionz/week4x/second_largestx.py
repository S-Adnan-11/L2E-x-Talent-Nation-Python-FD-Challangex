def step(largest, second_largest, x):
    if largest is None or x > largest:
        return x, largest
    if x != largest and (second_largest is None or x > second_largest):
        return largest, x
    return largest, second_largest


def second_largest(nums):
    largestx = None
    runnerx = None
    for numberx in nums:
        # step hands back the new state; it doesn't sneakily edit anything.
        largestx, runnerx = step(largestx, runnerx, numberx)
    return runnerx


if __name__ == "__main__":
    try:
        numsx = [float(bitx) for bitx in input("Numbers, separated by spaces: ").split()]
        resultx = second_largest(numsx)
        print("Need at least two unique numbers." if resultx is None else resultx)
    except ValueError:
        print("Use numbers only.")
