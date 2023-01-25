# class Solution:
#     def containsDuplicate(self, nums: list[int]) -> bool:
#         seen = {}
#         for num in nums:
#             if seen.get(num) is not None:
#                 return True
#             else:
#                 seen[num] = True
#         return False


# class Solution:
#     def containsDuplicate(self, nums: list[int]) -> bool:
#         if len(nums) == 1:
#             return False
#         sort_nums = sorted(nums)
#         for c, v in enumerate(sort_nums):
#             if v == sort_nums[c -1]:
#                 return True
#         return False

from collections import Counter

class Solution:
    def containsDuplicate(self, nums: list[int]) -> bool:
        c = Counter(nums)
        for item in c.keys():
            if c[item] > 1:
                return True
        return False
