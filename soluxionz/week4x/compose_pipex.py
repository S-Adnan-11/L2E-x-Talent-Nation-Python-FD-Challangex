def compose(f, g):
    def composedx(x):
        return f(g(x))
    return composedx


def pipe(*funcs):
    def pipedx(x):
        resultx = x
        for funcx in funcs:
            resultx = funcx(resultx)
        return resultx
    return pipedx


def strip(textx):
    return textx.strip()


def lower(textx):
    return textx.lower()


def remove_vowels(textx):
    return "".join(charx for charx in textx if charx.lower() not in "aeiou")


def reverse(textx):
    charsx = []
    indexx = len(textx) - 1
    while indexx >= 0:
        charsx.append(textx[indexx])
        indexx -= 1
    return "".join(charsx)


def reverse_recursive(textx, indexx=None):
    if indexx is None:
        indexx = len(textx) - 1
    if indexx < 0:
        return ""
    return textx[indexx] + reverse_recursive(textx, indexx - 1)


if __name__ == "__main__":
    add_onex = lambda x: x + 1
    doublex = lambda x: x * 2
    print("Compose:", compose(add_onex, doublex)(5))
    print("Pipe:", pipe(add_onex, doublex)(5))
    pipelinex = pipe(strip, lower, remove_vowels, reverse)
    textx = input("Text for the pipeline: ")
    print(pipelinex(textx))
    print("Recursive reverse bonus:", reverse_recursive(textx))
