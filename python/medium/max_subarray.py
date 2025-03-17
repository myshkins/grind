class Solution:
    def maxSubArray(self, nums: list[int]) -> int:
        big = -inf
        if len(nums) == 1:
            return nums[0]
        for c, v in enumerate(nums[1:]):
            nums[c+1] = max(v, (nums[c] + v))
            if nums[c+1] > big:
                big = nums[c+1]
        return big

test1 = [5,4,-1,7,8]
test2 = [1]
s = Solution()
print(s.maxSubArray(test1))