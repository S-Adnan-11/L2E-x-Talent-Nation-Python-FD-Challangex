def averagex(scoresx):
    if not scoresx:
        return None
    totalx = 0
    for scorex in scoresx:
        if not 0 <= scorex <= 100:
            raise ValueError("Scores must be between 0 and 100.")
        totalx += scorex
    return totalx / len(scoresx)


def letter_gradex(avgx):
    if avgx is None:
        return "N/A"
    if avgx >= 70:
        return "A"
    if avgx >= 60:
        return "B"
    if avgx >= 50:
        return "C"
    if avgx >= 45:
        return "D"
    if avgx >= 40:
        return "E"
    return "F"


def student_reportx(studentsx):
    reportx = []
    highestx = None
    lowestx = None
    for studentx in studentsx:
        avgx = averagex(studentx["scores"])
        rowx = (studentx["name"], avgx, letter_gradex(avgx))
        reportx.append(rowx)
        if avgx is None:
            continue  # No scores ≠ zero marks, so this one sits out the ranking.
        if highestx is None or avgx > highestx[1]:
            highestx = rowx
        if lowestx is None or avgx < lowestx[1]:
            lowestx = rowx
    return reportx, highestx, lowestx


if __name__ == "__main__":
    studentsx = [
        {"name": "Sam", "scores": [80, 90]},
        {"name": "David", "scores": [55, 60]},
    ]
    reportx, highestx, lowestx = student_reportx(studentsx)
    for namex, avgx, gradex in reportx:
        displayx = "N/A" if avgx is None else f"{avgx:.2f}"
        print(f"{namex} → Average: {displayx} → Grade: {gradex}")
    for labelx, rowx in (("Highest", highestx), ("Lowest", lowestx)):
        if rowx is None:
            print(f"{labelx}: None")
        else:
            print(f"{labelx}: {rowx[0]} ({rowx[1]:.2f})")
