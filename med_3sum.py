"""
classic 3sum problem, solution is to:
1. find all paris
2. sort the number array
3, for each pair binary search for third element that completes sum

*note* this solution doesn't work, too slow and doesn't catch the triple zero case
"""
from itertools import combinations


class Solution:
    def bsearch(self, target: int, arr: list) -> int | bool:
        lo = 0
        hi = len(arr) - 1
        while lo <= hi:
            mid = lo + (hi - lo) // 2
            if target < arr[mid][0]:
                hi = mid - 1
            elif target > arr[mid][0]:
                lo = mid + 1
            else:
                return arr[mid]
        return "False"

    def threeSum(self, nums: list[int]) -> list[list[int]]:
        """
        Given an integer array nums, return all the triplets [nums[i], nums[j],
        nums[k]] such that i != j, i != k, and j != k, and nums[i] + nums[j] +
        nums[k] == 0.
        """
        result = []
        seen = set()
        num_arr = [(nums[i], i) for i in range(len(nums))]
        s_arr = sorted(num_arr, key=lambda x: x[0])
        pairs = list(combinations(num_arr, 2))
        for pair in pairs:
            t = -(pair[0][0] + pair[1][0])
            if t in seen:
                continue
            seen.add(t)
            third = self.bsearch(t, s_arr)
            if third != "False" and (third[1] != pair[0][1] and third[1] != pair[1][1]):
                triplet = [pair[0][0], pair[1][0], third[0]]
                set_triplet = frozenset(triplet)
                if set_triplet not in seen:
                    seen.add(set_triplet)
                    result.append(triplet)
        return result

num1 = [-1,0,1,2,-1,-4]
num2 = [0, 0, 0]
# Output: [[-1,-1,2],[-1,0,1]]
s = Solution()
print(s.threeSum(num2))
