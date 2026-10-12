matrixx = [[2, 4, 6], [1, 3, 5], [10, 20, 30]]

row_num = 1
for row in matrixx:            # out loop
    total = 0
    for num in row:        # inn loop
        total += num
    print("Row", row_num, "total:", total)
    row_num += 1
    