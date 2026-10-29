sentence = input("Enter a sentence: ")

capitalized = ""
no_spaces = ""
start_of_word = True            


for character in sentence:
    if character == " ":
        capitalized += character        
        start_of_word = True    
    else:
        if start_of_word and character >= "a" and character <= "z":
            character = chr(ord(character) - 32)
        capitalized += character
        no_spaces += character
        start_of_word = False

print("Capitalized:", capitalized)
print("No Spaces:", no_spaces)
