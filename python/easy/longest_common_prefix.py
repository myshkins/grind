class Solution:
    def longestCommonPrefix(self, strs: list[str]) -> str:
        prefix = strs[0]
        for s in strs:
            for c, v in enumerate(prefix):
                if c + 1 > len(s) or v != s[c]:
                    prefix = prefix[0:c]
                    break
        return prefix