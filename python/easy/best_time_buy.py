# class Solution:        
#     def maxProfit(self, prices) -> int:
#         max_profit = None
#         min_price = None
#         pot_min = None
#         for count, value in enumerate(prices[:-1]):
#             if (profit := prices[count + 1] - value) > 0:
#                 if min_price is None:
#                     min_price = value
#                     pot_min = min_price
#                 if max_profit is None:
#                     max_profit = profit
#                 if value < pot_min:
#                     pot_min = value
#                 if (prices[count + 1] - pot_min) > max_profit:
#                     max_price = prices[count + 1]
#                     min_price = pot_min
#         if max_price is None:
#             return 0
#         else:
#             return max_price - min_price

class Solution:        
    def maxProfit(self, prices) -> int:
        max_profit = 0
        min_price = prices[0]
        pot_min = prices[0]
        for count, value in enumerate(prices):
            if value < pot_min:
                pot_min = value
            if (profit := (value - pot_min)) > max_profit:
                max_profit = profit
        return max_profit

input1 = [7,1,5,3,6,4]
#output 5
input2 = [7,6,4,3,1]
#output 0
input3 = [5,2,3,0,3,5,6,8,1,5]
#output 8
input4 = [1, 2]
#output 1
input5 = [2,1,2,1,0,1,2]
#output 2
input6 = [3,3,5,0,0,3,1,4]
#output 4
s = Solution()
print(s.maxProfit(input6))