class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        

        max_profit = 0
        current_profit = 0
        L = 0

        for R in range(1,len(prices)):

            if prices[L] < prices[R]:
                current_profit = prices[R] - prices[L]
                max_profit = max(max_profit,current_profit)
            else:
                L = R

        return max_profit


        