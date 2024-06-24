import heapq
import copy

def newstates(puzzle):
    newstate = []
    for i in range(3):
        for j in range(3):
            if puzzle[i][j] == 0:
                if i - 1 >= 0:
                    temp = puzzle[i - 1][j]
                    puzzle[i][j] = puzzle[i - 1][j]
                    puzzle[i - 1][j] = 0
                    newstate.append((heuristic(puzzle), copy.deepcopy(puzzle)))
                    puzzle[i - 1][j] = temp
                    puzzle[i][j] = 0
                if i + 1 < 3:
                    temp = puzzle[i + 1][j]
                    puzzle[i][j] = puzzle[i + 1][j]
                    puzzle[i + 1][j] = 0
                    newstate.append((heuristic(puzzle), copy.deepcopy(puzzle)))
                    puzzle[i + 1][j] = temp
                    puzzle[i][j] = 0
                if j - 1 >= 0:
                    temp = puzzle[i][j - 1]
                    puzzle[i][j] = puzzle[i][j - 1]
                    puzzle[i][j - 1] = 0
                    newstate.append((heuristic(puzzle), copy.deepcopy(puzzle)))
                    puzzle[i][j - 1] = temp
                    puzzle[i][j] = 0
                if j + 1 < 3:
                    temp = puzzle[i][j + 1]
                    puzzle[i][j] = puzzle[i][j + 1]
                    puzzle[i][j + 1] = 0
                    newstate.append((heuristic(puzzle), copy.deepcopy(puzzle)))
                    puzzle[i][j + 1] = temp
                    puzzle[i][j] = 0
                break  # Stop after finding the blank tile
    return newstate

def heuristic(puzzle):
    count = 0
    for i in range(3):
        for j in range(3):
            if puzzle[i][j] != goal[i][j]:
                count += 1
    return count

def BestFS(start, goal):
    visited = set()
    pq = [(heuristic(start), start, [])]  # Include the path as well
    heapq.heapify(pq)
    while pq:
        _, current, path = heapq.heappop(pq)
        if current == goal:
            print("Path taken:")
            for p in path:
                for row in p:
                    print(row)
                print()
            print("Solution found:")

            return True
        visited.add(tuple(map(tuple, current)))
        for h, state in newstates(current):
            if tuple(map(tuple, state)) not in visited:
                heapq.heappush(pq, (h, state, path + [state]))  # Update the path
    print("No solution found.")
    return False

start = [[1, 2, 3], [7, 8, 4], [6, 0, 5]]
goal = [[1, 2, 3], [8, 0, 4], [7, 6, 5]]
print("Enter the Start state")
for i in range(0,3):
     for j in range(0,3):
          start[i][j]=int(input())
print("Enter the Goal state")
for i in range(0,3):
     for j in range(0,3):
          goal[i][j]=int(input())
print("The start state is")
for row in start:
     print(row)
BestFS(start, goal)
