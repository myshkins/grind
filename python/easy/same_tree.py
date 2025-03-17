# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p, q) -> bool:
        result = [True]
        def dfs(nodep, nodeq):
            if not result[0]:
                return
            if nodep is None:
                return
            if nodep.val != nodeq.val:
                result[0] = False
                return
            dfs(nodep.left, nodeq.left)
            dfs(nodep.right, nodeq.right)
        dfs(p, q)
        return result[0]