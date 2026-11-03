def rle_encode(text):
    if text == "":
        return ""
    if not text.isalpha():
        raise ValueError("RLE text must contain letters only.")
    result = ""
    i = 0
    while i < len(text):
        current = text[i]
        count = 0
        while i < len(text) and text[i] == current:
            count += 1
            i += 1
        result += current + str(count)
    return result


def rle_decode(encoded):
    result = ""
    i = 0
    while i < len(encoded):
        letter = encoded[i]
        if not letter.isalpha():
            raise ValueError("Each run must start with a letter.")
        i += 1
        digits = ""
        while i < len(encoded) and "0" <= encoded[i] <= "9":
            digits += encoded[i]
            i += 1
        if digits == "" or int(digits) < 1:
            raise ValueError("Each letter needs a positive count.")
        result += letter * int(digits)
    return result


def compression_ratio(text):
    if text == "":
        return 0.0
    return len(rle_encode(text)) / len(text)


if __name__ == "__main__":
    for text in ("aaabbc", "aaaaaaaaaaaab", "", "a", "AaAa", "aabbaa"):
        encoded = rle_encode(text)
        decoded = rle_decode(encoded)
        print(repr(text), "→", repr(encoded), "→", repr(decoded),
              "Round trip:", decoded == text)
    print("Compression ratio for abcd:", compression_ratio("abcd"))
    print("abcd gets longer cos every single letter needs a count too.")
