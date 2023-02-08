"""
approach is to do initial processing of matrix, by finding all zeros and adding
them to the queue. if an item is not zero it's marked -1 to indicate it has not
yet been processed (note this saves space over maintaining a separate `seen`
data structure). then continue with bfs of queue. look at each neighbor and
mark it as origin plus one, then add it to the queue.
"""
from collections import deque


class Solution:
    def updateMatrix(self, mat: list[list[int]]) -> list[list[int]]:
        q = deque([])
        dirs = [(0, 1), (1, 0), (-1, 0), (0, -1)]
        rows = len(mat)
        cols = len(mat[0])
        for r in range(rows):
            for c in range(cols):
                if mat[r][c] == 0:
                    q.append((r, c))
                else:
                    mat[r][c] = -1
        while q:
            r, c = q.popleft()
            for i in range(4):
                nr, nc = (r + dirs[i][0]), (c + dirs[i][1])
                if (
                    nc < 0
                    or nr < 0
                    or nc == cols
                    or nr == rows
                    or mat[nr][nc] != -1
                ):
                    continue
                mat[nr][nc] = mat[r][c] + 1
                q.append((nr, nc))
        return mat


input1 = [[0, 0, 0], [0, 1, 0], [0, 0, 0]]
input2 = [[0, 0, 0], [0, 1, 0], [1, 1, 1]]
s = Solution()
answer = s.updateMatrix(input2)
print(answer)
