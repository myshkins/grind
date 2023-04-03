"""
classic 3sum problem, solution is to:
1. find all paris
2. sort the number array
3, for each pair binary search for third element that completes sum

"""


class Solution:
    def bsearch(self, target: int, arr: list) -> int | bool:
        lo = 0
        hi = len(arr) - 1
        while lo <= hi:
            mid = lo + (hi - lo) // 2
            if target < arr[mid]:
                hi = mid - 1
            elif target > arr[mid]:
                lo = mid + 1
            else:
                return arr[mid]
        return False


    def threeSum(self, nums: list[int]) -> list[list[int]]:
        """
        Given an integer array nums, return all the triplets [nums[i], nums[j],
        nums[k]] such that i != j, i != k, and j != k, and nums[i] + nums[j] +
        nums[k] == 0.
        """
        res = []
        negatives, positives, zeros = [], [], []
        seen = set()
        nums_sorted = sorted(nums)
        for num in nums_sorted:
            if num < 0:
                negatives.append(num)
            elif num > 0:
                positives.append(num)
            else:
                zeros.append(num)

        if zeros:
            for num in nums_sorted:
                fz_triplet = frozenset([num, 0, -1 * num])
                if self.bsearch((-1 * num), nums_sorted) and fz_triplet not in seen:
                    seen.add(fz_triplet)
                    res.append([num, 0, -1 * num])

        for i in range(len(negatives)):
            for j in range(i+1, len(negatives)):
                p, q = negatives[i], negatives[j]
                target = -1 * (p + q)
                complement = self.bsearch(target, positives)
                if complement:
                    triplet = sorted([p, q, target])
                    fs_triplet = frozenset(triplet)
                    if fs_triplet not in seen:
                        res.append(triplet)
                        seen.add(fs_triplet)

        for i in range(len(positives)):
            for j in range(i+1, len(positives)):
                p, q = positives[i], positives[j]
                target = -1 * (p + q)
                complement = self.bsearch(target, negatives)
                if complement:
                    triplet = sorted([p, q, target])
                    fs_triplet = frozenset(triplet)
                    if fs_triplet not in seen:
                        res.append(triplet)
                        seen.add(fs_triplet)

        if len(zeros) >= 3:
            res.append([0, 0, 0])

        return res

num1 = [-1,0,1,2,-1,-4]
num2 = [0, 0, 0]
# Output: [[-1,-1,2],[-1,0,1]]
s = Solution()
print(s.threeSum(num1))
