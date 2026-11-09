def is_balanced(text) -> bool:
    bracks = {"}": "{",
            "]": "[",
            ")": "("}

    pairing = []

    for x in text:
        if x in "{([":
            pairing.append(x)
        elif x in "}])":
            if len(pairing) == 0:
                return False

            last_brack = pairing.pop()
            if last_brack != bracks[x]:
                return False

    if len(pairing) != 0:
        return False
    else:
        return True


def max_depth(text) -> int:
    if not is_balanced(text):
        raise ValueError("Not balanced so no max depth chicken")
    depth = 0
    deepest = 0
    for x in text:
        if x in "{([":
            depth += 1
            if depth > deepest:  # keep the peak, not the final balance 😭
                deepest = depth
        elif x in "}])":
            depth -= 1
    return deepest


if __name__ == "__main__":
    for text in ("(a + b) * [c - d]", "{[()]}", "([)]", "((", "}{", "",
                 "{{[[()]]}}", "()[]]", "((a)(b))", "plain text"):
        balanced = is_balanced(text)
        print(repr(text), "→", balanced)
        if balanced:
            print("Max depth:", max_depth(text))
