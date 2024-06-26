import random

def heuristic(board):
    conflicts = 0
    for i in range(len(board)):
        for j in range(i+1, len(board)):
            if board[i] == board[j] or abs(i - j) == abs(board[i] - board[j]):
                conflicts += 1
    return conflicts

def solve_queens(initial_board):
    current_board = initial_board.copy()
    current_heuristic = heuristic(current_board)
    same_state_count = 0
    max_same_state_count = 3 

    while current_heuristic > 0:
        print("Current Board:", current_board)
        print("Current Heuristic:", current_heuristic)

        # Generate a random move (swap two rows)
        row1, row2 = random.sample(range(1, 9), 2)
        current_board[row1-1], current_board[row2-1] = current_board[row2-1], current_board[row1-1]

        new_heuristic = heuristic(current_board)
        if new_heuristic < current_heuristic:
            current_heuristic = new_heuristic
            same_state_count = 0  # Reset same state counter
        else:
            # Undo the move if it doesn't lead to improvement
            current_board[row1-1], current_board[row2-1] = current_board[row2-1], current_board[row1-1]
            same_state_count += 1

        if same_state_count >= max_same_state_count:
            # Perform a random move to a neighboring state
            row1, row2 = random.sample(range(1, 9), 2)
            current_board[row1-1], current_board[row2-1] = current_board[row2-1], current_board[row1-1]
            same_state_count = 0  # Reset same state counter

    print("Solution Found!")
    print("Final Board:", current_board)
    print("Final Heuristic:", current_heuristic)

# Example usage:
initial_board = []
t=8
print("Initial Board")
while t:
    inp=int(input())
    initial_board.append(inp)
    t=t-1   # Initial board (can be user input)
solve_queens(initial_board)
