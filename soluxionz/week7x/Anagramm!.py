def count_letters(text):
    counts = {}    
    for letter in text:
        if letter in counts:
            counts[letter] += 1
        else:
            counts[letter] = 1
    return counts


first = input("First word: ").lower()
second = input("Second word: ").lower()

if count_letters(first) == count_letters(second):
    print("Anagram")
else:
    print("Not an anagram")
