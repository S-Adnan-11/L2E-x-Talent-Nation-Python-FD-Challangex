def play_hangman(word, guesses, max_attempts):
    if not isinstance(max_attempts, int) or max_attempts < 0:
        raise ValueError("Attempts must be a non-negative integer.")
    for letter in word:
        if not "a" <= letter <= "z":
            raise ValueError("The word must contain lowercase a-z letters only.")
    display = ["_"] * len(word)
    guessed = []
    wrong_guesses = []
    missing = len(word)
    if missing == 0:
        return "won", "", wrong_guesses
    if max_attempts == 0:
        return "lost", "".join(display), wrong_guesses

    for guess in guesses:
        if len(guess) != 1 or not "a" <= guess <= "z":
            raise ValueError("Each guess must be one lowercase a-z letter.")
        if guess in guessed:
            continue  
        guessed.append(guess)
        found = False
        for i in range(len(word)):
            if word[i] == guess:
                display[i] = guess
                missing -= 1
                found = True
        if not found:
            wrong_guesses.append(guess)
        if missing == 0:
            return "won", "".join(display), wrong_guesses
        if len(wrong_guesses) >= max_attempts:
            return "lost", "".join(display), wrong_guesses
    return "playing", "".join(display), wrong_guesses


def main():
    try:
        word = input("Hidden word (a-z): ").strip().lower()
        max_attempts = int(input("Wrong guesses allowed: "))
        guesses = []
        status, display, wrong = play_hangman(word, guesses, max_attempts)
        while True:
            print(display, "| Remaining:", max_attempts - len(wrong))
            if status != "playing":
                print(status)
                break
            guess = input("One letter: ").strip().lower()
            if len(guess) != 1 or not "a" <= guess <= "z":
                print("One a-z letter pls.")
                continue
            guesses.append(guess)
            status, display, wrong = play_hangman(word, guesses, max_attempts)
    except ValueError as error:
        print(error)
    except (EOFError, KeyboardInterrupt):
        print("\nGame exited.")


if __name__ == "__main__":
    cases = [("apple", ["a", "z", "p", "l", "e"], 3),
             ("python", ["a", "b", "c", "d"], 3),
             ("loop", ["l", "o", "o", "p"], 3),
             ("code", ["c", "z", "z", "o"], 2), ("z", [], 1)]
    for word, guesses, attempts in cases:
        print(word, guesses, "→", play_hangman(word, guesses, attempts))
    main()
