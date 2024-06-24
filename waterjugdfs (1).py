# -*- coding: utf-8 -*-
"""
Created on Sun Mar  3 13:15:28 2024

@author: anish
"""
class WaterJug:
    def __init__(self, jug1_capacity, jug2_capacity, target):
        self.jug1_capacity = jug1_capacity
        self.jug2_capacity = jug2_capacity
        self.target = target
        self.visited_states = set()
        self.all_paths = []

    def dfs(self, jug1, jug2, path):
        if (jug1, jug2) in self.visited_states:
            return

        path.append((jug1, jug2))
        self.visited_states.add((jug1, jug2))

        if jug1 == self.target:
            self.all_paths.append(path[:])

        # Fill jug1
        self.dfs(self.jug1_capacity, jug2, path)

        # Fill jug2
        self.dfs(jug1, self.jug2_capacity, path)

        # Empty jug1
        self.dfs(0, jug2, path)

        # Empty jug2
        self.dfs(jug1, 0, path)

        # Pour from jug1 to jug2
        amount = min(jug1, self.jug2_capacity - jug2)
        self.dfs(jug1 - amount, jug2 + amount, path)

        # Pour from jug2 to jug1
        amount = min(jug2, self.jug1_capacity - jug1)
        self.dfs(jug1 + amount, jug2 - amount, path)

        path.pop()

    def find_all_paths(self):
        self.dfs(0, 0, [])
        return self.all_paths


# Get user input for jug capacities and target amount
jug1_capacity = int(input("Enter the capacity of the first jug: "))
jug2_capacity = int(input("Enter the capacity of the second jug: "))
target = int(input("Enter the target amount: "))

water_jug = WaterJug(jug1_capacity, jug2_capacity, target)
paths = water_jug.find_all_paths()

print("All Possible Paths:")
for path in paths:
    print("solution >>>")
    print(path)
