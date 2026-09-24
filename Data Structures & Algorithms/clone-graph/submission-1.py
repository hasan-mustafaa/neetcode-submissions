"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return
        
        start = node
        old_to_new = {}
        stack = [start]
        visited = set()

        while stack:
            node = stack.pop()
            old_to_new[node] = Node(val=node.val)

            for neighbor in node.neighbors:
                if neighbor not in visited:
                    stack.append(neighbor)
                    visited.add(neighbor)
            
        
        for old_node, new_node in old_to_new.items():
            for old_neighbor in old_node.neighbors:
                new_neighbor = old_to_new[old_neighbor]
                new_node.neighbors.append(new_neighbor)
        

        return old_to_new[start]