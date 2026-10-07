def simple_calcx(input_1, input_2, operator):
    if input_2 == 0 and operator == '/':
        return "Error: Division by zero is not allowed."
    elif operator == "+":
        return input_1 + input_2
    elif operator == "-":
        return input_1 - input_2
    elif operator == "*":
        return input_1 * input_2
    elif operator == "/":
        return input_1 / input_2
    return "Error: Use +, -, * or /."


if __name__ == "__main__":
    totalx = 0.0
    historyx = []
    print("calcx ready 😼 type + 5, * 2, undo or quit")
    print(f"Result: {totalx:g}")

    while True:
        try:
            commandx = input("> ").strip()
        except (EOFError, KeyboardInterrupt):
            print("\ncalcx out ✌️")
            break

        if commandx.lower() in ("quit", "exit"):
            break
        if commandx.lower() == "undo":
            if historyx:
                totalx = historyx.pop()
                print(f"Result: {totalx:g}")
            else:
                print("Nothing to undo yet.")
            continue

        bitsx = commandx.split()
        if len(bitsx) != 2:
            print("Use an operator and a number, lyk + 2.5")
            continue
        operator, numberx = bitsx
        try:
            numberx = float(numberx)
        except ValueError:
            print("That number isn't valid.")
            continue
        if numberx != numberx or numberx in (float("inf"), -float("inf")):
            print("Use a finite number.")
            continue

        resultx = simple_calcx(totalx, numberx, operator)
        if isinstance(resultx, str):
            print(resultx)
        elif resultx != resultx or resultx in (float("inf"), -float("inf")):
            print("Result is too big for this calculator.")
        else:
            # Save BEFORE changing it, so undo actually takes us back 😹
            historyx.append(totalx)
            totalx = resultx
            print(f"Result: {totalx:g}")
