def binary_search(nums, target) -> tuple[int, int]:
    low = 0
    high = len(nums) - 1
    indexxed = -1
    comparisons = 0

    while low <= high:
        middle = (low + high) // 2
        comparisons += 1
        if nums[middle] == target:
            indexxed = middle
            high = middle - 1 
        else:
            comparisons += 1
            if nums[middle] < target:
                low = middle + 1
            else:
                high = middle - 1
    return indexxed, comparisons


def binary_search_recursive(nums, target):
    def search(low, high):
        if low > high:
            return -1, 0
        middle = (low + high) // 2
        if nums[middle] == target:
            indexxed, comparisons = search(low, middle - 1)
            if indexxed == -1:
                indexxed = middle
            return indexxed, comparisons + 1
        if nums[middle] < target:
            indexxed, comparisons = search(middle + 1, high)
        else:
            indexxed, comparisons = search(low, middle - 1)
        return indexxed, comparisons + 2

    return search(0, len(nums) - 1)


if __name__ == "__main__":
    cases = [([1, 3, 3, 3, 5, 8], 3), ([1, 3, 5, 8], 4),
             ([], 7), ([5], 5), ([2, 2, 2, 2], 2), ([-5, -2, 0, 4], -2)]
    print("Comparisons count each == or < check against the target.")
    for nums, target in cases:
        loop_answer = binary_search(nums, target)
        recursive_answer = binary_search_recursive(nums, target)
        print(nums, "target:", target, "→", loop_answer,
              "Match" if loop_answer == recursive_answer else "Mismatch")
