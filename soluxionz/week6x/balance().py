sentence = input("Enter a string: ")


pairs = {")": "(", "]": "[", "}": "{"}

stack = []
balanced = True

for x in sentence:
    if x == "(" or x == "[" or x == "{":
        stack.append(x)
    elif x == ")" or x == "]" or x == "}":
        if len(stack) == 0:
            balanced = False
            break
        last_open = stack.pop()  # last open, first out 😼
        if last_open != pairs[x]:
            balanced = False
            break

if len(stack) != 0:
    balanced = False

if balanced:
    print("Balanced")
else:
    print("Not balanced")
