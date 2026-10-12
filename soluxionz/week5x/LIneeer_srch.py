values = [14, 7, 22, 9, 7, 31]
print("Enter only numbers pls \n")
target = int(input("Target: "))

indexxed = -1

for i in range(len(values)):
    if values[i] == target:
        indexxed = i
        break  

if indexxed == -1:
    print("Target not found")
else:
    print("Found at index", indexxed)