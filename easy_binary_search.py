class Solution:
    def search(self, nums, target: int) -> int:
        answer = [-1]
        def inner_search(lo, hi):
            mid = lo + ((hi - lo) // 2)
            if nums[mid] == target:
                answer[0] = mid
            if lo + 1 == hi:
                return
            if nums[mid] > target:
                inner_search(lo, mid)
            elif nums[mid] < target:
                inner_search(mid, hi)
        inner_search(0, len(nums))
        return answer[0]


nums1 = [5]
target1 = 5
#Output: 4
#Explanation: 9 exists in nums and its index is 4

s = Solution()
print(s.search(nums1, target1))