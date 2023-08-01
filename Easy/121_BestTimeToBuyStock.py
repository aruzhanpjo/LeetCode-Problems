"""
You are given an array prices where prices[i] is the price of a given stock on the ith day.

You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock.

Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.
"""

# help with the solution and sliding window algorithm from Neetcode.
# need to revise!!

#runtime - 895ms, beats 94.06%, memory - 27.38MB, beats 64.49%

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l, r = 0, 1
        Mprofit = 0

        while r<len(prices):
            if prices[r]>prices[l]:
                profit= prices[r]-prices[l]
                Mprofit = max(Mprofit, profit)

            else:
                l=r
            r+=1

        return Mprofit

