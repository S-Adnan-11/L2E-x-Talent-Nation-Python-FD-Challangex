def hanoi(n, source, target, helper):
    if not isinstance(n, int) or n < 0:
        raise ValueError("Disk count must be a non-negative integer.")
    if n == 0:
        return []
    moves = hanoi(n - 1, source, helper, target)
    moves.append((source, target))
    moves.extend(hanoi(n - 1, helper, target, source))
    return moves


if __name__ == "__main__":
    print("Moves for 3 disks:", hanoi(3, "A", "C", "B"))
    for n in range(1, 11):
        print("Disks:", n, "Moves:", len(hanoi(n, "A", "C", "B")))
    print("Each count is double the previous count plus one: 2**n - 1.")
    for n in range(1, 13):
        print("Count check", n, "→", len(hanoi(n, "A", "C", "B")) == 2 ** n - 1)
    print("Zero disks:", hanoi(0, "A", "C", "B"))
