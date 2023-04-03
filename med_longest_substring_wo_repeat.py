"""
Given a string s, find the length of the longest substring without repeating
characters.

strategy: use a variation of Kadane's algorithm, which is originally for finding
subarray with largest sum. it goes in O(n). calculates the max sum for any
subarry ending at a[i] as the max of either a[i] or a[i]+ a[i-1]
"""


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        result = start = 0
        seen = {}
        for c, v in enumerate(s):
            if seen.get(v) is not None and start <= seen[v]:
                start = seen[v] + 1
            else:
                result = max(result, c - start + 1)
            seen[v] = c
        return result

s = Solution()
print(s.lengthOfLongestSubstring("tmmzuxt"))