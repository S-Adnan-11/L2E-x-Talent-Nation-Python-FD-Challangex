def game_status(board):
    if len(board) != 3:
        return "Invalid"
    x_count = 0
    o_count = 0
    empty = False
    for row in board:
        if len(row) != 3:
            return "Invalid"
        for square in row:
            if square == "X":
                x_count += 1
            elif square == "O":
                o_count += 1
            elif square == " ":
                empty = True
            else:
                return "Invalid"
    if abs(x_count - o_count) > 1:
        return "Invalid"

    winners = {}
    for i in range(3):
        if board[i][0] != " " and board[i][0] == board[i][1] == board[i][2]:
            winners[board[i][0]] = True
        if board[0][i] != " " and board[0][i] == board[1][i] == board[2][i]:
            winners[board[0][i]] = True
    if board[0][0] != " " and board[0][0] == board[1][1] == board[2][2]:
        winners[board[0][0]] = True
    if board[0][2] != " " and board[0][2] == board[1][1] == board[2][0]:
        winners[board[0][2]] = True
    if len(winners) == 2:
        return "Invalid"
    if "X" in winners:
        return "X wins"
    if "O" in winners:
        return "O wins"
    return "In progress" if empty else "Draw"


if __name__ == "__main__":
    boards = [
        [["X", "X", "X"], ["O", "O", " "], [" ", " ", " "]],
        [["O", "X", "X"], ["X", "O", " "], [" ", " ", "O"]],
        [["X", "O", "X"], ["O", "X", "O"], ["O", "X", "O"]],
        [["X", " ", " "], [" ", "O", " "], [" ", " ", " "]],
        [[" ", " ", " "], [" ", " ", " "], [" ", " ", " "]],
        [["O", "O", " "], [" ", " ", " "], ["X", "X", "X"]],
        [["O", " ", "X"], ["O", " ", "X"], [" ", " ", "X"]],
        [["X", "X", "X"], ["O", "O", "O"], [" ", " ", " "]],
    ]
    for board in boards:
        print(board, "→", game_status(board))
