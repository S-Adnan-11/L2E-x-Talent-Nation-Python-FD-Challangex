def insertion_sort(nums: list[int]) -> tuple[int, int]:
    comparisons = 0
    shifts = 0
    for x in range(1, len(nums)):
        key = nums[x]
        left = x - 1
        while left >= 0:
            comparisons += 1
            if nums[left] <= key:
                break
            nums[left + 1] = nums[left]
            shifts += 1
            left -= 1
        nums[left + 1] = key  # gap made, key goes here 😼
    return comparisons, shifts


def bubble_sort(nums, descending=False):
    comparisons = 0
    swaps = 0
    end = len(nums) - 1
    while end > 0:
        swapped = False
        for i in range(end):
            comparisons += 1
            if descending:
                out_of_order = nums[i] < nums[i + 1]
            else:
                out_of_order = nums[i] > nums[i + 1]
            if out_of_order:
                nums[i], nums[i + 1] = nums[i + 1], nums[i]
                swaps += 1
                swapped = True
        if not swapped:
            break
        end -= 1
    return comparisons, swaps


if __name__ == "__main__":
    for listed in ([5, 2, 4, 1], [1, 2, 3, 4], [4, 3, 2, 1], [], [2, 2, -1]):
        before = listed.copy()
        counts = insertion_sort(listed)
        print(before, "→", listed, "Comparisons, shifts:", counts)
    for n in (10, 20):
        ascending = list(range(n))
        descending = list(range(n, 0, -1))
        print("Size:", n, "Sorted:", insertion_sort(ascending),
              "Reversed:", insertion_sort(descending))
    print("Sorted work grows roughly with n; reversed work grows with n squared.")
    cases = [[1, 2, 4, 3, 5], [1, 2, 3, 4, 5], [5, 4, 3, 2, 1], [], [2, -1, 2, 0]]
    for listed in cases:
        first = listed.copy()
        second = listed.copy()
        print("Bonus:", listed, "Insertion:", insertion_sort(first),
              "Week 8 bubble:", bubble_sort(second), "Match:", first == second)
    print("Insertion does fewer comparisons on the nearly sorted example: it stops at each key's gap.")

