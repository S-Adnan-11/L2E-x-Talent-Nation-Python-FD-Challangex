matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

"""

[
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9],
]

"""

n = len(matrix)

print("Before:")
for row in matrix:
    print(row)


for i in range(n):
    for j in range(i + 1, n):
        temp = matrix[i][j]
        matrix[i][j] = matrix[j][i]
        matrix[j][i] = temp

for row in matrix:
    left = 0
    right = n - 1
    while left < right:
        temp = row[left]
        row[left] = row[right]
        row[right] = temp
        left += 1
        right -= 1

print("After:")
for row in matrix:
    print(row)
