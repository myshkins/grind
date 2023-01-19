import csv 

class Solution:
    def __init__(self):
        self.i = 0  #pointers left end
        self.j = 0
        self.p = 0  #pointers right end
        self.q = 0
        self.max = []  # [max value, start, end]
    
    def read_input(self):
        with open('max_subarray_input.txt', mode='r') as file:
            data = csv.reader(file)
            lst = list(data)
            lst[0][0] = 5356
            lst[0][-1] = -1163
            lst = list(map(int, lst[0]))
            return lst

    def maxSubArray(self, nums: list) -> int:
        self.p = (len(nums) - 1) # set pointers at right end
        self.q = self.p
        self.max = [nums[self.i], self.i, self.i] #arbitrary initialization
        def compare(n):
            self.i = self.i + n
            self.p = self.p - n
            headsum = sum(nums[self.p:self.q + 1])
            tailsum = sum(nums[self.j:self.i + 1])
            if headsum > self.max[0]:
                self.max = [headsum, self.p, self.q]
            if tailsum > self.max[0]:
                self.max = [tailsum, self.j, self.i]
            
            if self.j == self.p:
                return
            if self.i > self.p:
                return
            if (tailsum < 0 and headsum >= 0) or (tailsum <= 0 and headsum > 0):
                self.i += 1
                self.j = self.i
            elif (headsum < 0 and tailsum >= 0) or (headsum <= 0 and tailsum > 0):
                self.p -= 1
                self.q = self.p
            elif tailsum < 0 and headsum < 0:
                if headsum <= tailsum:
                    self.p -= 1
                    self.q = self.p
                elif tailsum < headsum:
                    self.i += 1
                    self.j = self.i
                else:
                    compare(1)
            elif tailsum >= 0 and headsum >= 0:
                compare(1)
            compare(0)
        compare(0)
        self.i = self.j
        self.p = self.q
        compare(0)
        result = max(self.max[0], sum(nums[self.j:self.q+1]))
        return result
            
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
nums5 = sol.read_input()
print(sol.maxSubArray(nums1))