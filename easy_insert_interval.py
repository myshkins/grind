class Solution:
    # def insert(self, intervals, newInterval):
    #     indx = next(i for i, v in enumerate(intervals) if v[0] > newInterval[0])
    #     intervals.insert(indx - 1, newInterval)
    #     if intervals[indx - 2][1] > intervals[indx -1][0]:
    #         intervals[indx - 2][1]             
    def insert(self, intervals, newInterval):
        for i, v in enumerate(intervals):
            if 


intervals1 = [[1,2],[3,5],[6,7],[8,10],[12,16]]
newInterval1 = [4,8]
#Output: [[1,2],[3,10],[12,16]]

intervals2 = [[1,3],[6,9]]
newInterval2 = [2,5]
#Output: 

intervals3 = [[1,5]]
newInterval3 = [2,5]
#Output: [[1,5]]

s = Solution()
print(s.insert(intervals1, newInterval1))