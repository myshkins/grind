# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        def inner_invert(node):
            if node.right is not None:
                inner_invert(node.right)
            if node.left is not None:
                inner_invert(node.lef)
            node.right, node.left = node.left, node.right
        inner_invert(root)
        return root
