# Define the goal state

goal_state = [[1, 4, 7],    

              [2, 5, 8],

              [3, 6, 0]]  # 0 represents the blank tile

 

# Function to calculate the number of misplaced tiles

def misplaced_tiles(state):

    count = 0

    for i in range(3):

        for j in range(3):

            if state[i][j] != goal_state[i][j]:

                count += 1

    return count

 

# Function to generate neighboring states by moving the blank tile

def generate_neighbors(state):

    neighbors = []

    blank_row, blank_col = find_blank_tile(state)

    directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]  # Right, Left, Down, Up

    for d in directions:

        new_row, new_col = blank_row + d[0], blank_col + d[1]

        if 0 <= new_row < 3 and 0 <= new_col < 3:

            new_state = [row[:] for row in state]  # Make a copy of the state

            new_state[blank_row][blank_col], new_state[new_row][new_col] = new_state[new_row][new_col], new_state[blank_row][blank_col]  # Swap tiles

            neighbors.append(new_state)

    return neighbors

 

# Function to find the position of the blank tile

def find_blank_tile(state):

    for i in range(3):

        for j in range(3):

            if state[i][j] == 0:

                return i, j

 

# Hill climbing algorithm

def hill_climbing(initial_state):

    current_state = initial_state

    while True:

        current_cost = misplaced_tiles(current_state)

        if current_cost == 0:  # Goal state reached

            return current_state

        neighbors = generate_neighbors(current_state)

        best_neighbor = min(neighbors, key=misplaced_tiles)

        current_state = best_neighbor

        h=misplaced_tiles(current_state)

        print("\nheuristic value=")

        print(h)

        for row in current_state:

            print(row)

        if misplaced_tiles(best_neighbor) >= current_cost:

            print("since in hill climbing the problem of local minima exists we need to stop here")

            return current_state

       

 

# Randomly generate initial state

 

# Main function

def main():

    initial_state = [[1, 4, 7],

              [0, 5, 8],

              [2, 3, 6]]

    print("Initial State:")

    h=misplaced_tiles(initial_state)

    print("heauristic value is")

    print(h)

    for row in initial_state:

        print(row)

    solution = hill_climbing(initial_state)

    print("\nSolution:")

    for row in solution:

        print(row)

 

if __name__ == "__main__":

    main()