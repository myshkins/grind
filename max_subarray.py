class Solution:
    def maxSubArray(self, nums: list) -> int:
        i = 0 #pointer for compares
        x, z = 0, len(nums) - 1 #pointers for subarray
        tail = []
        total = sum(nums)
        while i < len(nums) - 1:
            tail.append(nums[i])
            if total + (tailsum := sum(tail)) < total:
                x = i + 1
                total -= tailsum
                tail = []
            i += 1
        tail = []
        while i > x:
            tail.append(nums[i])
            if total + (tailsum := sum(tail)) < total:
                z = i - 1
                total -= tailsum
                tail = []
            i -= 1
        return total
            
nums2 = [-1, -2]
#Output: 6
nums1 = [-2,1,-3,4,-1,2,1,-5,4]
#Output: 6

sol = Solution()
print(sol.maxSubArray(nums2))