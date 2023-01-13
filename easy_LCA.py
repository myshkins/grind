# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def get_route(root: 'TreeNode', node: 'TreeNode') -> list:
        x = root
        path = []
        while node.val != x.val:
            path.append(x)
            if node.val < x.val:
                x = x.left
            else:
                x = x.right
        return path

    def lowestCommonAncestor(
        self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode'
        ) -> 'TreeNode':
        path_p = self.get_route(root, p)
        if q in path_p:
            return q
        path_q = self.get_route(root, q)
        if p in path_q:
            return p
        for node in path_p[::-1]:
            if node in path_q:
                return node