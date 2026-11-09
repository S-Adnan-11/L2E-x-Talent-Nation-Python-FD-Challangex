def spiral_order(matrix):
    if not matrix:
        return []
    columns = len(matrix[0])
    for row in matrix:
        if len(row) != columns:
            raise ValueError("Matrix rows must have the same length.")
    result = []
    top = 0
    bottom = len(matrix) - 1
    left = 0
    right = columns - 1
    while top <= bottom and left <= right:
        for column in range(left, right + 1):
            result.append(matrix[top][column])
        top += 1
        for row in range(top, bottom + 1):
            result.append(matrix[row][right])
        right -= 1
        if top <= bottom:
            for column in range(right, left - 1, -1):
                result.append(matrix[bottom][column])
            bottom -= 1
        if left <= right:  # don't walk an already used column again 😼
            for row in range(bottom, top - 1, -1):
                result.append(matrix[row][left])
            left += 1
    return result


def spiral_fill(n):
    if not isinstance(n, int) or n < 0:
        raise ValueError("Size must be a non-negative integer.")
    matrix = []
    for row in range(n):
        line = []
        for column in range(n):
            line.append(0)
        matrix.append(line)
    top, bottom = 0, n - 1
    left, right = 0, n - 1
    number = 1
    while top <= bottom and left <= right:
        for column in range(left, right + 1):
            matrix[top][column] = number
            number += 1
        top += 1
        for row in range(top, bottom + 1):
            matrix[row][right] = number
            number += 1
        right -= 1
        if top <= bottom:
            for column in range(right, left - 1, -1):
                matrix[bottom][column] = number
                number += 1
            bottom -= 1
        if left <= right:
            for row in range(bottom, top - 1, -1):
                matrix[row][left] = number
                number += 1
            left += 1
    return matrix


if __name__ == "__main__":
    cases = [[[1, 2, 3], [4, 5, 6], [7, 8, 9]], [[1, 2, 3, 4], [5, 6, 7, 8]],
             [[1], [2], [3]], [], [[7, 8, 9]], [[4]], [[], []]]
    for matrix in cases:
        print(matrix, "→", spiral_order(matrix))
    for n in (0, 1, 3, 4):
        print("Fill", n, "→", spiral_fill(n))
