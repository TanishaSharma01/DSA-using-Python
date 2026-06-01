# Leetcode 102 Medium
# Time Complexity O(N)
# Space Complexity O(N)
from collections import deque
from typing import Optional, List


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        # empty tree nothing to return
        if root == None: #if not root
            return []
        result = [] # final list of levels
        queue = deque([root]) # double ended queue, add root

        # until queue not empty
        while queue:
            level_size = len(queue) # number of nodes at the current level
            current_level = []  # values for this level

            # process exactly that many nodes
            for _ in range(level_size):
                node = queue.popleft() # pop from queue (FIFO)
                current_level.append(node.val)
                # pop from queue (FIFO)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            # after finishing this level, add it to result
            result.append(current_level)
        return result