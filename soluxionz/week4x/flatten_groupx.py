def flatten(nested):
    flatx = []

    def walkx(indexx):
        if indexx >= len(nested):
            return
        itemx = nested[indexx]
        if isinstance(itemx, list):
            flatx.extend(flatten(itemx))
        else:
            flatx.append(itemx)
        # Recursion handles the next sibling too. No sneaky loop in here 😹
        walkx(indexx + 1)

    walkx(0)
    return flatx


def group_by(items, key_fn):
    groupsx = {}
    for itemx in items:
        keyx = key_fn(itemx)
        if keyx not in groupsx:
            groupsx[keyx] = []
        groupsx[keyx].append(itemx)
    return groupsx


def group_by_recursive(items, key_fn):
    groupsx = {}

    def collectx(indexx):
        if indexx >= len(items):
            return
        itemx = items[indexx]
        keyx = key_fn(itemx)
        if keyx not in groupsx:
            groupsx[keyx] = []
        groupsx[keyx].append(itemx)
        collectx(indexx + 1)

    collectx(0)
    return groupsx


def first_letterx(wordx):
    return wordx[0].lower() if wordx else ""


def combined(nested):
    return group_by(flatten(nested), first_letterx)


if __name__ == "__main__":
    print(flatten([1, [2, [3, [4]], 5]]))
    wordsx = [["apple", "avocado"], ["banana"], [["cherry"]]]
    print(combined(wordsx))
    print("Recursive group bonus:", group_by_recursive(flatten(wordsx), first_letterx))
