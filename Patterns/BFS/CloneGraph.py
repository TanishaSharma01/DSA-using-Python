# Leetcode 133 Medium

# Time complexity O(V+E)
# Space complexity O(V)
"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

from typing import Optional


class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return node

        start = node
        o_to_n = {}
        stk = [start]
        visited = set()
        visited.add(start)

        # Copy nodes
        while stk:
            node = stk.pop()
            o_to_n[node] = Node(val=node.val)
            for nei in node.neighbors:
                if nei not in visited:
                    visited.add(nei)
                    stk.append(nei)

        # copy their edges
        for old_node, new_node in o_to_n.items():
            for nei in old_node.neighbors:
                new_nei = o_to_n[nei]
                new_node.neighbors.append(new_nei)

        return o_to_n[start]
