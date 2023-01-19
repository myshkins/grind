class Solution:
    def maxSubArray(self, nums: list) -> int:
        dp = [[0]*len(nums) for i in range(2)]
        dp[0][0], dp[1][0] = nums[0], nums[0]
        for i in range(1, len(nums)):
            dp[1][i] = max(nums[i], nums[i] + dp[1][i-1])
            dp[0][i] = max(dp[0][i-1], dp[1][i])
        return dp[0][-1]

nums4 = [-2, -3, -1]
#output -1
nums3 = [1, -1, 1]
#output 1            
nums2 = [-1, -2]
#Output: -1
nums1 = [-2,1,-3,4,-1,2,1,-5,4]
#Output: 6
nums6 = [-3, 1, -2, 2]
#output: 2
nums7 = [-1, -1, -2, -2]
nums8 = [0, 0, -3, 1]
nums9 = [3,-2,-3,-3,1,3,0]
numsA = [2,-1,-1,2,0,-3,3]

s = Solution()
print(s.maxSubArray(nums1))