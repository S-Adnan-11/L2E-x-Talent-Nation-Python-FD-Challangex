def pascal_rows(n) -> list[list[int]]:
    if not isinstance(n, int) or n < 0:
        raise ValueError("Row count must be a non-negative integer.")
    rows = []
    for row_num in range(n):
        row = [1]
        if row_num > 0:
            previous = rows[row_num - 1]
            for i in range(1, len(previous)):
                row.append(previous[i - 1] + previous[i])
            row.append(1)
        rows.append(row)
    return rows


def pascal_row(k):
    if not isinstance(k, int) or k < 0:
        raise ValueError("Row index must be a non-negative integer.")
    row = [1]
    for row_num in range(1, k + 1):
        row.append(1)
        i = len(row) - 2
        while i > 0:
            row[i] += row[i - 1]  # right to left keeps the old neighbours intact 
            i -= 1
    return row


if __name__ == "__main__":
    for n in (5, 1, 0, 3):
        print("Rows for", n, "→", pascal_rows(n))
    lines = []
    for row in pascal_rows(5):
        line = ""
        for number in row:
            if line:
                line += " "
            line += str(number)
        lines.append(line)
    for line in lines:
        print(" " * ((len(lines[-1]) - len(line)) // 2) + line)
    print("One-list bonus, row 4:", pascal_row(4))
