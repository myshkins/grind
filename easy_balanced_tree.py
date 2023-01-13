# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# class Solution:
#     def isBalanced(self, root: 'TreeNode') -> bool:
#         depths = []
#         def dfs(node, depth):
#             if not node.left and not node.right:
#                 depths.append(depth)
#             if node.right:
#                 dfs(node.right, depth+1)
#             if node.left:
#                 dfs(node.left, depth+1)
#         dfs(root, 0)
#         if len(depths) == 0:
#             return 'true'
#         elif (min(depths) + 1) < max(depths):
#             return 'false'
#         else:
#             return 'true' 

class Solution:
    def isBalanced(self, root: 'TreeNode') -> bool:
        result = True
        def dfs(node):
            nonlocal result
            if not node:
                return -1
            lh = dfs(node.left)
            rh = dfs(node.right)
            if abs(lh - rh) > 1:
                result = False
            return 1 + max(lh, rh)
        
        dfs(root)
        return result
        

root = TreeNode()
root.val = 1
root.left = TreeNode()
root.left.val = 2
root.left.left = TreeNode()
root.left.left.val = 3
root.left.left.left = TreeNode()
root.left.left.left.val = 4
root.left.left.right = TreeNode()
root.left.left.right.val = 4
root.left.right = TreeNode()
root.left.right.val = 3
root.right = TreeNode()
root.right.val = 2

groot = TreeNode()
groot.val = 3
groot.left = TreeNode()
groot.left.val = 9
groot.right = TreeNode()
groot.right.val = 20
groot.right.left = TreeNode()
groot.right.left.val = 15
groot.right.right = TreeNode()
groot.right.right.val = 7

s = Solution()
print(s.isBalanced(root))
