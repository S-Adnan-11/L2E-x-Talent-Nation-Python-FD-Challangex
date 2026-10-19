"oh"

listed = [12, 5, 27, 8, 14, 27, 3]


minn = listed[0]
minn_index = 0
maxx = listed[0]
maxx_index = 0
total = 0

for i in range(len(listed)):
    x = listed[i]
    total += x
    if x < minn:
        minn = x
        minn_index = i
    if x > maxx:
        maxx = x
        maxx_index = i

average = total / len(listed)

# average first, then count 😼
above_average = 0
for x in listed:
    if x > average:
        above_average += 1

print("Input list:", listed)
print("Smallest:", minn, "(at index", str(minn_index) + ")")
print("Largest:", maxx, "(at index", str(maxx_index) + ")")
print("Total:", total)
print("Average:", round(average, 2))
print("Numbers above average:", above_average)
