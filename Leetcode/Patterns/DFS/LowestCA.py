# Leetcode 236 Medium

# T: O(N)
# S: O(1)

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        # Base case: if we reach a null node, return None (no LCA found here)
        if not root:
            return None

        # If the current node is either p or q, return it
        # Because the current node itself is part of the ancestor chain
        if root == p or root == q:
            return root

        # Search recursively in the left and right subtrees
        l = self.lowestCommonAncestor(root.left, p, q)
        r = self.lowestCommonAncestor(root.right, p, q)

        # If both left and right calls return a non-None value:
        # - that means one node (p or q) was found in the left subtree
        # - and the other node was found in the right subtree
        # So the current root is their lowest common ancestor
        if l and r:
            return root

        # Otherwise, return whichever side is non-None:
        # - if only left side found something, return l
        # - if only right side found something, return r
        # - if neither side found anything, returns None
        return l or r
