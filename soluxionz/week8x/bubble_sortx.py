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
    for listed in ([5, 1, 4, 2, 8], [1, 2, 3, 4, 5], [5, 4, 3, 2, 1],
                   [], [7], [2, -1, 2, 0]):
        before = listed.copy()
        comparisons, swaps = bubble_sort(listed)
        print(before, "→", listed, "Comparisons:", comparisons, "Swaps:", swaps)
    listed = [1, 4, 2, 4, -3]
    counts = bubble_sort(listed, descending=True)
    print("Descending:", listed, "Counts:", counts)
