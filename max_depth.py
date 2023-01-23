# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root):
        def dfs(node):
            if node is None:
                return 1
            depth = 1 + max(dfs(node.left), dfs(node.right))
            return depth
        return dfs(root) - 1