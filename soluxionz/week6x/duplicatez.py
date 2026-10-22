numbers = [1, 2, 3, 2, 4, 5, 1, 3, 2, 6, 8, 4, 4, 3, 8]

duplicates = []

for number in numbers:
    times = 0
    for other in numbers:
        if other == number:
            times += 1

    if times > 1 and number not in duplicates:  #actuallu n1!😹
        duplicates.append(number)

print(duplicates)

counts = {}
for number in numbers:
    if number in counts:
        counts[number] += 1
    else:
        counts[number] = 1

duplicate_counts = {}
for number in counts:
    if counts[number] > 1:
        duplicate_counts[number] = counts[number]

print(duplicate_counts)
