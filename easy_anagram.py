class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        s = [x for x in s]
        t = [x for x in t]
        s.sort()
        t.sort()
        for i in range(len(s)):
            if s[i] != t[i]:
                return False
        return True

s, t = "anagram", "nagaram"
s1, t1 = 'rat', 'car'


sol = Solution()
print(sol.isAnagram(s1, t1))
    # def isAnagram(self, s: str, t: str) -> bool:
    #     tlist = [y for y in t]
    #     for c in s:
    #         try:
    #             tlist.remove(c)
    #         except ValueError:
    #             return False
    #     if len(tlist) == 0:
    #         return True
    #     else:
    #         return False