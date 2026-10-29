A = [[1, 2], [3, 4]]
B = [[5, 6], [7, 8]]

rows_a = len(A)
cols_a = len(A[0])
rows_b = len(B)
cols_b = len(B[0])

if cols_a != rows_b:
    print("Cannot multiply: columns of A must equal rows of B.")
else:
    result = []
    for i in range(rows_a):                   
        new_row = []
        for j in range(cols_b):               
            total = 0
            for k in range(cols_a):    
                total += A[i][k] * B[k][j]
            new_row.append(total)
        result.append(new_row)

    print("Product Matrix:")
    for row in result:
        print(row)
