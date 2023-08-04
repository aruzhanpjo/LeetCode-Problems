"""
You are given an integer array prices where prices[i] is the price of a given stock on the ith day.

On each day, you may decide to buy and/or sell the stock. You can only hold at most one share of the stock at any time. However, you can buy it then immediately sell it on the same day.

Find and return the maximum profit you can achieve.
"""


#used brute force

#runtime - 53ms, beats 99.61%, memory - 17.70MB, beats 65.30%

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l, r = 0, 1
        maxProfit = []
        profit=0

        while r<len(prices):
            if prices[l]>prices[r]:
                l=r
                r+=1

            else:
                if r+1<len(prices) and prices[r+1]<prices[r]:
                    profit = prices[r]-prices[l]
                    maxProfit.append(profit)
                    l=r
                    r+=1
                    
                elif r==len(prices)-1 and prices[r]>prices[l]:
                    profit = prices[r]-prices[l]
                    maxProfit.append(profit)
                    r+=1
                    
                else:
                    r+=1
                #l=r

        return sum(maxProfit)
                