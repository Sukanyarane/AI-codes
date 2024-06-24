# -*- coding: utf-8 -*-
"""
Created on Sun Mar  3 13:23:04 2024

@author: anish
"""

from collections import deque

class WaterJug:
    def __init__(self, jug1_capacity, jug2_capacity, target):
        self.jug1_capacity = jug1_capacity
        self.jug2_capacity = jug2_capacity
        self.target = target
        self.visited_states = set()
        self.all_paths = []

    def bfs(self):
        queue = deque([(0, 0, [])])

        while queue:
            jug1, jug2, path = queue.popleft()

            if (jug1, jug2) in self.visited_states:
                continue

            path.append((jug1, jug2))
            self.visited_states.add((jug1, jug2))

            if jug1 == self.target:
                self.all_paths.append(path[:])

            # Fill jug1
            queue.append((self.jug1_capacity, jug2, path[:]))

            # Fill jug2
            queue.append((jug1, self.jug2_capacity, path[:]))

            # Empty jug1
            queue.append((0, jug2, path[:]))

            # Empty jug2
            queue.append((jug1, 0, path[:]))

            # Pour from jug1 to jug2
            amount = min(jug1, self.jug2_capacity - jug2)
            queue.append((jug1 - amount, jug2 + amount, path[:]))

            # Pour from jug2 to jug1
            amount = min(jug2, self.jug1_capacity - jug1)
            queue.append((jug1 + amount, jug2 - amount, path[:]))

        return self.all_paths


def get_positive_integer(prompt):
    while True:
        try:
            value = int(input(prompt))
            if value <= 0:
                print("Please enter a positive integer.")
            else:
                return value
        except ValueError:
            print("Please enter a valid integer.")


# Get user input for jug capacities and target amount
jug1_capacity = get_positive_integer("Enter the capacity of the first jug: ")
jug2_capacity = get_positive_integer("Enter the capacity of the second jug: ")
target = get_positive_integer("Enter the target amount: ")

# Find all possible paths using BFS
water_jug = WaterJug(jug1_capacity, jug2_capacity, target)
paths = water_jug.bfs()

# Display all possible paths
print("All Possible Paths:")
for path in paths:
    print("solution >>>")
    print(path)
