# Only the optional reduce exercises live here. Required soluxionz import nothing.
from functools import reduce


def most_frequent_reduce(freq):
    def choosex(winnerx, wordx):
        if winnerx is None or freq[wordx] > freq[winnerx]:
            return wordx
        return winnerx

    winnerx = reduce(choosex, freq, None)
    return "" if winnerx is None else winnerx


def two_sum_reduce(nums, target):
    def trackx(statex, indexedx):
        seenx, answerx = statex
        if answerx:
            return statex
        indexx, numberx = indexedx
        neededx = target - numberx
        if neededx in seenx:
            return seenx, [seenx[neededx], indexx]
        if numberx not in seenx:
            seenx[numberx] = indexx
        return seenx, answerx

    # This dict belongs to this call only. Copying it at every step would cost O(n²).
    return reduce(trackx, enumerate(nums), ({}, []))[1]


def second_largest_reduce(nums):
    def step_reducex(statex, numberx):
        largestx, runnerx = statex
        if largestx is None or numberx > largestx:
            return numberx, largestx
        if numberx != largestx and (runnerx is None or numberx > runnerx):
            return largestx, numberx
        return statex

    return reduce(step_reducex, nums, (None, None))[1]


if __name__ == "__main__":
    print("Most frequent:", most_frequent_reduce({"python": 2, "is": 2, "fun": 1}))
    print("Two sum:", two_sum_reduce([2, 7, 11, 15], 9))
    print("Second largest:", second_largest_reduce([4, 9, 2, 9, 7]))
