class Solution:
    # def isPalindrome(self, s: str) -> bool:
        # x = [c.lower() for c in s if c.isalnum()]
        # front = x[0:(len(x) // 2)]
        # back = x[-1:-(len(x) // 2 + 1):-1]
        # return (front == back)

    def isPalindrome(self, s: str) -> bool:
        x = [c.lower() for c in s if c.isalnum()]
        return x[0:(len(x) // 2)] == x[-1:-(len(x) // 2 + 1):-1]


test1 = "A man, a plan, a canal: Panama"
#true

test2 = "race a car"
#true

test3 = " "
#true

test4 = "bo oboo!B"

sol = Solution()
sol.isPalindrome(test4)