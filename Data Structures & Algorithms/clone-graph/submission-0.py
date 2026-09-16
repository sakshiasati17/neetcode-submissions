"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional["Node"]) -> Optional["Node"]:
        if not node:
            return None

        copies = {}

        def dfs(current):
            if current in copies:
                return copies[current]

            copied_current = Node(current.val)
            copies[current] = copied_current

            for neighbor in current.neighbors:
                copied_neighbor = dfs(neighbor)
                copied_current.neighbors.append(copied_neighbor)

            return copied_current

        return dfs(node)
        




        