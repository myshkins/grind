from collections import Counter
import itertools as it

class Solution:
    def longestPalindrome(self, s: str) -> int:
        c = Counter(s)
        p = 0
        for v in c.values():
            if v >= 2:
                p += (v - (v%2))
        try:
            odd = next(v for v in c.values() if v % 2 == 1)
            if odd:
                p += 1
        except StopIteration:
            pass
        return p

s = Solution()

print(s.longestPalindrome("aabccdeh"))