class Solution:
    def majorityElement(self, nums: list[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        seen = {}
        for num in nums:
            count = seen.get(num)
            if not count:
                seen[num] = 1
            else:
                seen[num] += 1
                if seen[num] >= (len(nums) / 2):
                    return num

nums = [3,2,3]
# Output: 2

s = Solution()
print(s.majorityElement(nums))