from copy import copy


class Solution:
    def insert(self, intervals: list[list], newInterval: list):
        left, right = [], []
        start, end = newInterval[0], newInterval[1]
        for i in intervals:
            if i[1] < start:
                left.append(i)
            elif i[0] > end:
                right.append(i)
            else:
                start = min(start, i[0])
                end = max(end, i[1])
        return left + [[start, end]] + right

intervals1 = [[1, 2], [3, 5], [6, 7], [8, 10], [12, 16]]
newInterval1 = [4, 8]
# Output: [[1,2],[3,10],[12,16]]

intervals2 = [[1, 3], [6, 9]]
newInterval2 = [2, 5]
# Output: [[1,5], [6, 9]]

intervals3 = [[1, 5]]
newInterval3 = [2, 5]
# Output: [[1,5]]

s = Solution()
print(s.insert(intervals1, newInterval1))
