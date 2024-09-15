from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_price = float("inf")
        max_profit = 0

        for i in prices:
            if i < min_price:
                min_price = i
            elif i - min_price > max_profit:
                print(i, min_price)
                max_profit = i - min_price

        return max_profit


obj = Solution()
print(obj.maxProfit(prices=[7, 1, 5, 3, 6, 4]))
