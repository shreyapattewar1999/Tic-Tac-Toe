board = ["-", "-", "-", "-", "-", "-", "-", "-", "-"]

def display_board(board):
    print()
    for i in range(0,9,3):
        print(board[i] + " | " + board[i+1]+ " | " + board[i+2])

    print()
# display_board(board)
def check_win(board, char):
    for i in range(0, 9, 3):
        if board[i]==char and board[i+1]==char and board[i+2]==char:
            return True

    j = 0
    while j<3:
        if board[j]==char and board[j+3]==char and board[j+6]==char:
            return True
        j+=1

    if board[0] == char and board[4] == char and board[8] == char:
        return True
    if board[2] == char and board[4] == char and board[6] == char:
        return True

    return False


def check_game_over(board):
    for i in range(len(board)):
        if board[i] == "-":
            return False

    print()
    print("GRID IS FULL")
    return True

game_over = False
turn = "X"
while not game_over:
    display_board(board)
    if turn == "X":
        print("Turn - X")
    else:
        print("Turn - O")
    position, char = input("Enter a position and character(X or O) : ").split(" ")
    position = int(position)
    position -= 1
    if char != turn:
        print("Its not your turn")
        continue

    if position < 0 or position > 8:
        print("You have entered wrong position number")
        continue

    if board[position] != "-":
        print(f"{position+1} is already filled")
        print("Please enter right position")
        continue

    board[position] = char
    win = check_win(board, char)
    # win_X = check_win(board, "X")
    # win_O = check_win(board, "O")

    if win:
        game_over = True
        print("*******************************************************")
        print(char+" wins")
    # elif win_O:
    #     game_over = True
    #     print("*******************************************************")
    #     print("O wins")

    if not game_over:
        game_over = check_game_over(board)
    if game_over:
        print("*********** Game Over *****************")

    turn = "O" if turn=="X" else "X"