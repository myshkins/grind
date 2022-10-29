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
    def __init__(self, root):
        self.root = root
        self.paths = [None for _ in range(10^4 + 1)]
        self.dist_to = [None for _ in range(10^4 + 1)]
        self.long_path = []

    def diameterOfBinaryTree(self, root: TreeNode) -> int:
        pass


    def dfs(self):
        def inner_search(node, dist):
            if node.right:
                self.paths[node.right.val] = node
                self.dist_to[node.right.val] = dist
                inner_search(node.right, (dist + 1))
            if node.left:
                self.paths[node.left.val] = node
                self.dist_to[node.left.val] = dist
                inner_search(node.left, (dist + 1))
        inner_search(self.root, 1)

    def get_diameter(self):
        far_ind = max(range(len(self.dist_to)), key=lambda x: 0 if self.dist_to[x]==None else self.dist_to[x])
        far_node = self.paths[far_ind]
        x = far_node
        while x is not None:
            self.long_path.append(x)
            x = self.paths[x.val]
        





connections = [None, (1, 2, 3), (2, 4, 5), (3, None, None), (4, 6, None), (5, None, 8), (6, None, None), (7, None, None), (8, 7, 10), (9, None, None), (10, None, 9),]

tree = Tree(connections)
tree.build_tree()
sol = Solution(tree.root)
sol.dfs()
print(sol.paths)
print(sol.dist_to)
print(sol.get_diameter())
print('hi')