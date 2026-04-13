class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        L =0 
        R = 0
        max_sum = 0

        while R < len(prices):
            if prices[R] < prices[L]:
                L = R
            elif prices[R] > prices[L]:
                max_sum = max(prices[R] - prices[L],max_sum)
            R += 1
        return max_sum
        