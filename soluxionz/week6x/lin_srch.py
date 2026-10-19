values = [14, 7, 22, 9, 7, 31, 7, 5]
target = int(input("Target: "))

indexxed = []

# all the matches this time lol 🔎
for i in range(len(values)):
    if values[i] == target:
        indexxed.append(i)

if len(indexxed) == 0:
    print("Target not found")
else:
    print("Found at indices:", indexxed,
          "| Count:", len(indexxed),
          "| First:", indexxed[0],
          "| Last:", indexxed[-1])
