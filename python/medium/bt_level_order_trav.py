# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def levelOrder(self, root: TreeNode) -> list[list[int]]:
        level = [root]
        res = []
        while True:
            temp = []
            for node in level:
                if node.right:
                    temp.append(node.right)
                if node.left:
                    temp.append(node.left)
            level_values = [node.val for node in level]
            res.append(level_values)
            level = temp
            if len(temp) == 0:
                break
        return res

root = TreeNode(
    val=3,
    left=TreeNode(
        val=9,
        left=None,
        right=None
    ),
    right=TreeNode(
        val=20,
        left=TreeNode(
            val=15,
            left=None,
            right=None
        ),
        right=TreeNode(
            val=7,
            left=None,
            right=None
    )
)
)

s = Solution()
print(s.levelOrder(root))