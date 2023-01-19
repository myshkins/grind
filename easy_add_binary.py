# class Solution:
#     def addBinary(self, a: str, b: str) -> str:
#         a_int = int(a, 2)
#         b_int = int(b, 2)
#         result = a_int + b_int
#         binary = bin(result)
#         result = binary.removeprefix('0b')
#         return result
import itertools as it

class Solution:
    def addBinary(self, a: str, b: str) -> str:
        if len(a) == len(b):
            long, short = a, b
        else:
            long = max(a, b, key=lambda x: len(x))
            short = min(a, b, key=lambda x: len(x))
            diff = len(long) - len(short)
            buffer = "".join(["0" for _ in it.repeat(None, diff)])
            short = (buffer + short)
        short = short[::-1]
        long = long[::-1]
        carry = 0
        result = []
        for c, v in enumerate(long):
            bsum = carry + int(v) + int(short[c])
            carry = 0
            if bsum == 1 or bsum == 3:
                result.append('1')
            if bsum == 2 or bsum == 0:
                result.append('0')
            if bsum >= 2:
                carry = 1
        if carry > 0:
            result.append('1')       
        final = ("".join(result))[::-1]
        return final
