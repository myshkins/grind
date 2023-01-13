# Definition for a binary tree node.

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Tree:
    def __init__(self, connections: list) -> None:
        self.root = None
        self.connections = connections
    
    def make_node(self, n):
        if n is None:
            return
        node = TreeNode(
            val=self.connections[n][0],
            left=(self.make_node(self.connections[n][1])),
            right=(self.make_node(self.connections[n][2])),)
        return node

    def build_tree(self):
        self.root = TreeNode(
            val=self.connections[1][0],
            left=self.make_node(self.connections[1][1]),
            right=self.make_node(self.connections[1][2]))
        if self.root is None:
            self.root = node

class Solution:
    def __init__(self):
        self.max = 0

    def diameterOfBinaryTree(self, root) -> int:
        def get_lengths(node):
            if node is None:
                return -1
            left = 1 + get_lengths(node.left)
            right = 1 + get_lengths(node.right)
            longest = max(left, right)
            diameter = left + right
            if diameter > self.max:
                self.max = diameter
            return longest
        get_lengths(root)
        return self.max


connections = [None, (1, 2, 3), (2, 4, 5), (3, None, None), (4, 6, None), (5, None, 8), (6, None, None), (7, None, None), (8, 7, 10), (9, None, None), (10, None, 9),]

tree = Tree(connections)
tree.build_tree()
sol = Solution()
print(sol.diameterOfBinaryTree(tree.root))
