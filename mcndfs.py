# -*- coding: utf-8 -*-
"""
Created on Mon Jun 24 16:56:30 2024

@author: Sukanya Rane
"""

from collections import deque

# Input: Number of Missionaries, Cannibals, and Boat size
m = int(input("No. of Missionaries: "))
c = int(input("No. of Cannibals: "))
b = int(input("Boat size: "))
allpaths = []

# Function to check if the state is valid
def is_valid(state):
    m1, c1, n = state
    m2 = m - m1
    c2 = c - c1
    # Check for negative numbers of missionaries or cannibals
    if m1 < 0 or m2 < 0 or c1 < 0 or c2 < 0:
        return False
    # Check if missionaries are outnumbered by cannibals on either side
    if (m1 and m1 < c1) or (m2 and m2 < c2):
        return False
    return True

# Function to generate all possible valid successor states
def generate_successors(state):
    m, c, n = state
    successors = []
    # Possible moves of missionaries and cannibals
    actions = [(1, 0), (2, 0), (0, 1), (0, 2), (1, 1)]
    
    for action in actions:
        moved_ms, moved_cn = action
        if n == 1:  # Boat is on the starting side
            new_state = (m - moved_ms, c - moved_cn, 0)
        else:  # Boat is on the opposite side
            new_state = (m + moved_ms, c + moved_cn, 1)
        if is_valid(new_state):
            successors.append(new_state)
    return successors

# Depth-First Search (DFS) to find all valid paths
def dfs():
    start_state = (m, c, 1)
    goal_state = (0, 0, 0)
    visited = set()
    stack = [(start_state, [])]
    
    while stack:
        current_state, path = stack.pop()
        if current_state in visited:
            continue
        path.append(current_state)
        if current_state == goal_state:
            allpaths.append(path)
            continue
        visited.add(current_state)
        for successor in generate_successors(current_state):
            if successor not in visited:
                stack.append((successor, path.copy()))

# Run DFS
dfs()

# Output the results
if len(allpaths) == 0:
    print("No Solutions")
else:
    for p in allpaths:
        print(p)