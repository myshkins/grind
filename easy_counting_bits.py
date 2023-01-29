class Solution:
    def countBits(self, n: int) -> list[int]:
        ans = []
        for p in range(n +1):
            binary = bin(p).removeprefix('0b')
            count = 0
            for bit in binary:
                if bit == "1":
                    count += 1
            ans.append(count)
        return ans

s = Solution()
print(s.countBits(10))