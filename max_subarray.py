import csv

class Solution:
    def maxSubArray(self, nums: list) -> int:
        i, j = 0, 0 #pointer for compares
        p = (len(nums) - 1) #pointers for maxSubArray
        q = p
        total = sum(nums)
        while i < p:
            if (tailsum := sum(nums[j:i + 1])) <= (headsum := sum(nums[p:q + 1])):
                if total + (tailsum) < total:
                    i += 1
                    j = i
                    total -= tailsum
                else:
                    i += 1
            else:
                if total + (headsum) < total:
                    p -= 1
                    q = p
                    total -= headsum
                else:
                    p -= 1
        return total

    def read_input(self):
        with open('max_subarray_input.txt', mode='r') as file:
            data = csv.reader(file)
            lst = list(data)
            lst[0][0] = 5356
            lst[0][-1] = -1163
            lst = list(map(int, lst[0]))
            return lst

nums4 = [-2, -3, -1]
#output -1
nums3 = [1, -1, 1]
#output 1            
nums2 = [-1, -2]
#Output: 6
nums1 = [-2,1,-3,4,-1,2,1,-5,4]
#Output: 6
nums6 = [-3, 1, -2, 2]
sol = Solution()
# nums5 = sol.read_input()
print(sol.maxSubArray(nums1))