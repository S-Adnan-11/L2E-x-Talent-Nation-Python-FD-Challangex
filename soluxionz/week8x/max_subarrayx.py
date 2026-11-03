def max_subarray_brute(nums):
    if not nums:
        return 0, -1, -1
    best = nums[0]
    best_start = 0
    best_end = 0
    for start in range(len(nums)):
        total = 0
        for end in range(start, len(nums)):
            total += nums[end]
            if total > best:
                best = total
                best_start = start
                best_end = end
    return best, best_start, best_end


def max_subarray_fast(nums):
    if not nums:
        return 0, -1, -1
    total = nums[0]
    best = nums[0]
    start = 0
    best_start = 0
    best_end = 0
    for i in range(1, len(nums)):
        if total < 0:  # carrying a negative total won't help the next number 😼
            total = nums[i]
            start = i
        else:
            total += nums[i]
        if total > best:
            best = total
            best_start = start
            best_end = i
    return best, best_start, best_end


if __name__ == "__main__":
    cases = [[-2, 1, -3, 4, -1, 2, 1, -5, 4], [5], [-3, -1, -2],
             [], [0, 0, 0], [2, -2, 2], [-7], [1, 2, 3]]
    for listed in cases:
        brute = max_subarray_brute(listed)
        fast = max_subarray_fast(listed)
        print(listed, "→", fast, "Match" if brute == fast else "Mismatch")
