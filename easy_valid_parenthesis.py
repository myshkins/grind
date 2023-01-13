class Solution:
    def isVAlid(self, s: str) -> bool:
        q = []
        d = {')':'(', ']':'[', '}':'{'}
        for x in s:
            if x in [')', ']', '}']:
                if q.pop() != d[x]:
                    return False
            if x in ['(', '[', '{']:
                q.append(x)
        if len(q) != 0:
            return False
        else:
            return True

test1 = "[()]{{}]"
sol = Solution()
print(sol.isVAlid(test1))