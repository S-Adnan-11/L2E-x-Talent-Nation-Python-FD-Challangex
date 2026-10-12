def balanced_px(sentence):
    par = 0

    for x in sentence:
        if x == "(":
            par += 1
        elif x == ")":
            par -= 1

        if par < 0:
            break


    if par == 0:
        print("Output: Balanced")
    else:
        print("Output: Not Balanced")
