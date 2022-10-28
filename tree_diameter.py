# Definition for a binary tree node.

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Tree:
    def __init__(self, connections: list) -> None:
        self.root = None
        self.connection = connections
    
    def build_tree(self):
        for n in self.connection:
            node = TreeNode(val=n[0], left=n[1], right=n[2])



class Solution:
    def diameterOfBinaryTree(self, root: TreeNode) -> int:
        self.root = root
        self.paths = [None for _ in range(10^4 + 1)]
        self.dist_to = [None for _ in range(10^4 + 1)]
    
    def dfs(self):
        def inner_search(node, dist):
            if node.right:
                self.paths[node.right] = node
                self.dist_to[node.right] = dist
                inner_search(node.right, (dist + 1))
            if node.left:
                self.paths[node.left.val] = node
                self.dist_to[node.left] = dist
                inner_search(node.left, (dist + 1))
        inner_search(self.root, 1)




connections = [(1, 2, 3), (3, None, None), (2, 4, 5), (4, None, None), (5, None, 8), (6, None, None), (8, 7, 10), (7, None, None), (10, None, 9), (9, None, None)]

tree = Tree(connections)
tree.build_tree()

sol = Solution()