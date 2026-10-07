def averagex(scoresx):
    if not scoresx:
        return None
    totalx = 0
    for scorex in scoresx:
        if not 0 <= scorex <= 100:
            raise ValueError("Scores must be between 0 and 100.")
        totalx += scorex
    return totalx / len(scoresx)


def grade_for(avg):
    if avg is None:
        return "N/A"
    if avg >= 70:
        return "A"
    if avg >= 60:
        return "B"
    if avg >= 50:
        return "C"
    if avg >= 45:
        return "D"
    if avg >= 40:
        return "E"
    return "F"


def student_rowx(studentx):
    avgx = averagex(studentx["scores"])
    return studentx["name"], avgx, grade_for(avgx)


def passedx(rowx):
    return rowx[2] in ("A", "B", "C")


def extremesx(rowsx):
    highestx = None
    lowestx = None
    for rowx in rowsx:
        if rowx[1] is None:
            continue
        if highestx is None or rowx[1] > highestx[1]:
            highestx = rowx
        if lowestx is None or rowx[1] < lowestx[1]:
            lowestx = rowx
    return highestx, lowestx


def student_reportx(studentsx):
    rowsx = list(map(student_rowx, studentsx))
    passesx = list(filter(passedx, rowsx))
    highestx, lowestx = extremesx(rowsx)
    return rowsx, passesx, highestx, lowestx


def rows_comprehensionx(studentsx):
    return [student_rowx(studentx) for studentx in studentsx]


if __name__ == "__main__":
    studentsx = [
        {"name": "Sam", "scores": [80, 90]},
        {"name": "David", "scores": [55, 60]},
    ]
    rowsx, passesx, highestx, lowestx = student_reportx(studentsx)
    for namex, avgx, gradex in rowsx:
        displayx = "N/A" if avgx is None else f"{avgx:.2f}"
        print(f"{namex} → Average: {displayx} → Grade: {gradex}")
    print("Passed (A–C):", [rowx[0] for rowx in passesx])
    for labelx, rowx in (("Highest", highestx), ("Lowest", lowestx)):
        if rowx is None:
            print(f"{labelx}: None")
        else:
            print(f"{labelx}: {rowx[0]} ({rowx[1]:.2f})")
    print("Comprehension bonus:", rows_comprehensionx(studentsx))
    # I find the comprehension clearer cos it reads as 'make a row for each student'.
