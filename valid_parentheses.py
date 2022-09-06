class Solution:
    def isValid(self, s: str) -> bool:
        for count, value in enumerate(s):
            if value == "(" and s[count + 1] != ")":
                return False
            if value == "{" and s[count + 1] != "}":
                return False
            if value == "[" and s[count + 1] != "]":
                return False
            return True



s1 = "()[]{}"
s2 = "({]])}"

solver = Solution()
print(solver.isValid(s2))