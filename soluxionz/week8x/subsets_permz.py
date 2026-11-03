def subsets(items):
    result = []
    current = []

    def choose(i):
        if i == len(items):
            result.append(current.copy())
            return
        choose(i + 1)
        current.append(items[i])
        choose(i + 1)
        current.pop()

    choose(0)
    return result


def permutations(items):
    result = []
    current = []
    used = [False] * len(items)

    def arrange():
        if len(current) == len(items):
            result.append(current.copy())
            return
        for i in range(len(items)):
            if not used[i]:
                used[i] = True
                current.append(items[i])
                arrange()
                current.pop()  # undo
                used[i] = False

    arrange()
    return result


def subsets_with_sum(items, target):
    result = []
    current = []

    def choose(i, total):
        if i == len(items):
            if total == target:
                result.append(current.copy())
            return
        choose(i + 1, total)
        current.append(items[i])
        choose(i + 1, total + items[i])
        current.pop()

    choose(0, 0)
    return result


if __name__ == "__main__":
    print("Subsets:", subsets([1, 2, 3]))
    print("Permutations:", permutations([1, 2, 3]))
    factorial = 1
    for n in range(9):
        if n > 0:
            factorial *= n
        items = list(range(n))
        print("n:", n, "Subsets:", len(subsets(items)), "Expected:", 2 ** n,
              "Permutations:", len(permutations(items)), "Expected:", factorial)
    for items, target in (([1, 2, 3], 3), ([], 0), ([-2, 1, 2], 0)):
        print("Sum bonus:", items, target, "→", subsets_with_sum(items, target))
