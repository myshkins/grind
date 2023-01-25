class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        s_res = []
        t_res = []
        for v in s:
            if v == "#":
                if len(s_res) > 0:
                    s_res.pop(len(s_res) - 1)
            else:
                s_res.append(v)
        for v in t:
            if v == "#":
                if len(t_res) > 0:
                    t_res.pop(len(t_res) - 1)
            else:
                t_res.append(v)
        return s_res == t_res

s = Solution()
print(s.backspaceCompare("ab##", "c#d#"))