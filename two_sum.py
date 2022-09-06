
class Solution:
    def twoSum(self, nums, target: int) -> list[int]:
        save_dict = {}
        for i in range((len(nums))):
            if nums[i] in save_dict:
                return [save_dict[nums[i]], i]
            else:
                save_dict[(target - nums[i])] = i


solve = Solution()

print(solve.twoSum([3, 2, 4], 6))
