# Leetcode 104 Easy
# Time complexity O(N) because we are visiting each node
# Space complexity O(h) where h is the tree height
from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        # if root is not null
        if root == None:
            return 0
        # left depth of the current node called
        left_depth = self.maxDepth(root.left)
        # right depth of the current node called
        right_depth = self.maxDepth(root.right)
        # 1 added because of root
        return max(left_depth, right_depth) + 1
