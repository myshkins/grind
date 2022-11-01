import csv

class Solution:
    def __init__(self):
        self.i = 0
        self.j = 0
        self.p = 0
        self.q = 0
        
    def maxSubArray(self, nums: list) -> int:
        i, j = 0, 0 #pointer for compares
        p = (len(nums) - 1) #pointers for maxSubArray
        q = p
        total = sum(nums)
        maximum = total
        # a, b = 0, 0     #subarray indices
        while i < p:
            if (tailsum := sum(nums[j:i + 1])) > maximum:
                maximum = tailsum
                # a, b = j, i
            if (headsum := sum(nums[p:q + 1])) > maximum:
                maximum = headsum
                # a, b = p, q
            if tailsum <= 0:
                j = i
            if headsum <= 0:
                q = p
            i += 1
            p -= 1
        return maximum

    def read_input(self):
        with open('max_subarray_input.txt', mode='r') as file:
            data = csv.reader(file)
            lst = list(data)
            lst[0][0] = 5356
            lst[0][-1] = -1163
            lst = list(map(int, lst[0]))
            return lst

    def sum(self, nums):
        print(sum(nums))

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
sol = Solution()
# nums5 = sol.read_input()
print(sol.maxSubArray(nums1))