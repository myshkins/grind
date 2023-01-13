from itertools import combinations

def climbStairs(n: int) -> int:
    def climb(n):  # inner function to make code simpler
        if n in memo:
            return memo[n]
        else:
            memo[n] = climb(n-1) + climb(n-2)
            return memo[n]
    memo = {1: 1, 2: 2}  # base cases
    return climb(n)


print(climbStairs(2))