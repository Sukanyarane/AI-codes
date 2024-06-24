import random

def print_board(board):
    print("-------------")
    for row in board:
        print("|", " | ".join(row), "|")
        print("-------------")

def check_winner(board, player):
    # Check rows
    for row in board:
        if all(cell == player for cell in row):
            return True

    # Check columns
    for col in range(3):
        if all(board[row][col] == player for row in range(3)):
            return True

    # Check diagonals
    if all(board[i][i] == player for i in range(3)) or all(board[i][2-i] == player for i in range(3)):
        return True

    return False

def get_empty_cells(board):
    return [(i, j) for i in range(3) for j in range(3) if board[i][j] == " "]

def minimax(board, depth, is_maximizing):
    if check_winner(board, "O"):
        return 1
    elif check_winner(board, "X"):
        return -1
    elif len(get_empty_cells(board)) == 0:
        return 0

    if is_maximizing:
        best_score = -float("inf")
        for i, j in get_empty_cells(board):
            board[i][j] = "O"
            score = minimax(board, depth+1, False)
            board[i][j] = " "
            best_score = max(score, best_score)
        return best_score
    else:
        best_score = float("inf")
        for i, j in get_empty_cells(board):
            board[i][j] = "X"
            score = minimax(board, depth+1, True)
            board[i][j] = " "
            best_score = min(score, best_score)
        return best_score

def get_best_move(board):
    best_score = -float("inf")
    best_move = None
    for i, j in get_empty_cells(board):
        board[i][j] = "O"
        score = minimax(board, 0, False)
        board[i][j] = " "
        if score > best_score:
            best_score = score
            best_move = (i, j)
    return best_move

def player_move(board):
    while True:
        try:
            row = int(input("Enter the row (1-3): ")) - 1
            col = int(input("Enter the column (1-3): ")) - 1
            if board[row][col] == " ":
                board[row][col] = "X"
                break
            else:
                print("That cell is already occupied. Try again.")
        except ValueError:
            print("Invalid input. Please enter a number.")

def play_game():
    board = [[" " for _ in range(3)] for _ in range(3)]
    print_board(board)

    while True:
        player_move(board)
        print_board(board)

        if check_winner(board, "X"):
            print("Congratulations! You won!")
            break

        if len(get_empty_cells(board)) == 0:
            print("It's a draw!")
            break

        ai_move = get_best_move(board)
        board[ai_move[0]][ai_move[1]] = "O"
        print("AI's Move:")
        print_board(board)

        if check_winner(board, "O"):
            print("AI wins! Better luck next time.")
            break

        if len(get_empty_cells(board)) == 0:
            print("It's a draw!")
            break

if __name__ == "__main__":
    play_game()
