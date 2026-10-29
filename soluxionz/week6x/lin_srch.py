values = [14, 7, 22, 9, 7, 31, 7, 5]
target = int(input("Target: "))

indices = []               

for i in range(len(values)):
    if values[i] == target:
        indices.append(i)  

if len(indices) == 0:
    print("Target not found")
else:
    print("Found at indices:", indices,
          "| Count:", len(indices),
          "| First:", indices[0],
          "| Last:", indices[-1])