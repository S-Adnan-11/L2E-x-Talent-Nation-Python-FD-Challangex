def clean_wordsx(textx):
    punctuationx = ",.!?;:\"'()[]{}<>/-_\\|@#$%^&*+=~`…—–“”‘’"
    cleanx = ""
    for charx in textx.lower():
        cleanx += " " if charx in punctuationx else charx
    return cleanx.split()


def count_words(words: list[str]) -> dict[str, int]:
    freqx = {}
    for wordx in words:
        wordx = wordx.lower()
        if wordx:
            freqx[wordx] = freqx.get(wordx, 0) + 1
    return freqx


def most_frequent(freq: dict[str, int]) -> str:
    winnerx = ""
    highestx = 0
    for wordx, countx in freq.items():
        if countx > highestx:
            winnerx = wordx
            highestx = countx
    # Strict > keeps the first word on a tie, matching the python example.
    return winnerx


if __name__ == "__main__":
    freqx = count_words(clean_wordsx(input("Paragraph: ")))
    winnerx = most_frequent(freqx)
    print(freqx)
    if winnerx:
        print(f"Most frequent word: {winnerx} ({freqx[winnerx]})")
    else:
        print("No words found.")
