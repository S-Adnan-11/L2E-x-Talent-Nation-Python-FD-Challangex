def word_frequencyx(textx):
    punctuationx = ",.!?;:\"'()[]{}<>/-_\\|@#$%^&*+=~`…—–“”‘’"
    cleanx = ""
    for charx in textx.lower():
        # Punctuation becomes a gap, so python,python doesn't turn into pythonpython.
        cleanx += " " if charx in punctuationx else charx

    freqx = {}
    for wordx in cleanx.split():
        freqx[wordx] = freqx.get(wordx, 0) + 1

    winnerx = ""
    highestx = 0
    for wordx, countx in freqx.items():
        if countx > highestx:
            winnerx = wordx
            highestx = countx
    return freqx, winnerx


if __name__ == "__main__":
    freqx, winnerx = word_frequencyx(input("Paragraph: "))
    print(freqx)
    if winnerx:
        print(f"Most frequent word: {winnerx} ({freqx[winnerx]})")
    else:
        print("No words found.")
