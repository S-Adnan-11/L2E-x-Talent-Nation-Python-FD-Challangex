matrixx = [[2, 4, 6], [1, 3, 5], [10, 20, 30]]

number_of_columns = len(matrixx[0])
column_totals = [0] * number_of_columns    

row_num = 1
for row in matrixx:
    total = 0
    for column in range(len(row)):
        total += row[column]
        column_totals[column] += row[column] 
    row_average = total / len(row)
    print("Row", row_num, "total:", total,
          "| Row", row_num, "average:", row_average)
    row_num += 1

print()
for column in range(number_of_columns):
    print("Column", column + 1, "total:", column_totals[column])
