from typing import Optional

# this is a dumb solution. doesn't take advantage of tree structure
# where left node is always smaller than the right

class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left: Optional[TreeNode] = None
        self.right: Optional[TreeNode]= None

class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
        """
        do a dfs for p and then another for q
        keep the path for each dfs
        compare paths to find lca
        """
        def dfs(
                node: Optional[TreeNode],
                target: int,
                path: list[TreeNode],
                visited: dict[int, bool]
                ) -> tuple[Optional[TreeNode], list[TreeNode], dict[int, bool]]:
            if node is None or visited.get(node.val):
                return None, path, visited
            if node.val == target:
                visited[node.val] = True
                path.append(node)
                return node, path, visited
            if node.right and not visited.get(node.right.val):
                node_found, path, visited = dfs(node.right, target, path, visited)
                if node_found:
                    path.append(node)
                    visited[node.val] = True
                    return node_found, path, visited
            if node.left and not visited.get(node.left.val):
                node_found, path, visited = dfs(node.left, target, path, visited)
                if node_found:
                    path.append(node)
                    visited[node.val] = True
                    return node_found, path, visited
            visited[node.val] = True
            return None, path, visited
        
        p_path = []
        p_visited = {}
        _, p_path, _ = dfs(root, p.val, p_path, p_visited)

        q_path = []
        q_visited = {}
        _, q_path, _ = dfs(root, q.val, q_path, q_visited)

        long_path = q_path
        short_path = p_path
        if len(p_path) > len(q_path):
            long_path, short_path = p_path, q_path
        for indx in range(-1, -(len(long_path))-1, -1):
            try:
                short_val = short_path[indx].val
            except IndexError:
                short_val = None
            if long_path[indx].val != short_val:
                return long_path[indx+1]
        return root

r = TreeNode(6)
eight = TreeNode(8)
nine = TreeNode(9)
seven = TreeNode(7)
two = TreeNode(2)
four = TreeNode(4)
zero = TreeNode(0)
three = TreeNode(3)
five = TreeNode(5)
r.right = eight
r.left = two
eight.right = nine
eight.left = seven
two.right = four
two.left = zero
four.right = five
four.left = three

# r = TreeNode(2)
# one = TreeNode(1)
# r.left = one
s = Solution()
answer = s.lowestCommonAncestor(root=r, p=two, q=four)
print(answer.val)
