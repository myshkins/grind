# The isBadVersion API is already defined for you.
arr = [False, True]
def isBadVersion(version: int) -> bool:
    return arr[version - 1]

class Solution:
    def __init__(self) -> None:
        pass
    def firstBadVersion(self, n: int) -> int:
        def search(low, hi):
            while low < hi:
                mid = (low + hi) // 2
                if not isBadVersion(mid):
                    low = mid + 1
                else:
                    hi = mid
            return low
        return search(1, n)

s = Solution()
print(s.firstBadVersion(n=2))