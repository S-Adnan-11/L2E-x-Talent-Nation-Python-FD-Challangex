def encode(text):
    if text == "":
        return ""

    result = ""
    current = text[0]    
    count = 1

    for i in range(1, len(text)):
        if text[i] == current:      
            count += 1
        else:
            result += current + str(count)
            current = text[i]
            count = 1

    result += current + str(count)  # last run needs saving too 😼
    return result


def decode(encoded):
    result = ""
    letter = ""
    digits = "" 

    for character in encoded:
        if character.isdigit():
            digits += character
        else:
            if letter != "":
                result += letter * int(digits)
            letter = character
            digits = ""

    if letter != "":
        result += letter * int(digits)
    return result


text = input("Enter a string: ")
encoded = encode(text)
print("Encoded:", encoded)
print("Decoded back:", decode(encoded))
