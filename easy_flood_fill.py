"""flood fill solution"""
from typing import List

class Solution:
    """flood fill solver"""
    def __init__(self):
        self.pixels_checked = {}
        self.image = None
        self.color = None
        self.old_color = None
        self.pixels = None

    def floodFill(
        self, image: List[List[int]], sr: int, sc: int, color: int
        ) -> List[List[int]]:
        """initializes flood fill attributes with parameters and then search"""
        self.image = image
        self.color = color
        self.old_color = image[sr][sc]
        self.pixels = [
            (x, y) for x in range(len(self.image)) 
            for y in range(len(self.image[0]))
            ]
        self.pixels_checked = {pixel:False for pixel in self.pixels}
        self.image[sr][sc] = color
        self.fill_neighbors(sr, sc)
        return self.image

    def fill_neighbors(self, sr: int, sc: int):
        """recursive depth-first search function"""
        neighbors = [
            (sr + 1, sc),
            (sr - 1, sc),
            (sr, sc + 1),
            (sr, sc - 1),
            ]
        for neighbor in neighbors:
            if (
                0 <= neighbor[0] < len(self.image) and
                0 <= neighbor[1] < len(self.image[0])
                ):
                # pixel = self.image[neighbor[0]][neighbor[1]]
                if (
                    not self.pixels_checked[neighbor] and 
                    self.image[neighbor[0]][neighbor[1]] == self.old_color
                    ):
                    self.image[neighbor[0]][neighbor[1]] = self.color
                    self.pixels_checked[neighbor] = True
                    self.fill_neighbors(neighbor[0], neighbor[1])


s = Solution()
image1 = [[0,0,0],[0,1,0]]
sr = 1
sc = 1
color = 2
# Output: [[2,2,2],[2,2,0],[2,0,1]]
result = s.floodFill(image1, sr, sc, color)
print(result)