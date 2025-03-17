from collections import Counter
# class Solution:
#     def canConstruct(self, ransomNote: str, magazine: str) -> bool:
#         if len(magazine) < len(ransomNote):
#             return False
#         letters = {}
#         for _ in magazine:
#             if not letters.get(_):
#                 letters[_] = 1
#             else:
#                 letters[_] += 1
#         for _ in ransomNote:
#             if not letters.get(_) or letters.get(_) == 0:
#                 return False
#             else:
#                 letters[_] -= 1
#         return True

class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        rc = Counter(ransomNote)
        mc = Counter(magazine)

        for k,v in rc.items():
            if k not in mc or mc[k] < v:
                return False
        
        return True
