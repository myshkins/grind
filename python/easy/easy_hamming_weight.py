class Solution:
    def hammingWeight(self, n: int) -> int:
        s = bin(n).removeprefix('0b')
        count = 0
        for c in s:
            if c == '1':
                count += 1
        return count


x = int('11111111111111111111111111111101', base=2)
y = int('00000000000000000000000000001011', base=2)
s = Solution()
print(s.hammingWeight(x))