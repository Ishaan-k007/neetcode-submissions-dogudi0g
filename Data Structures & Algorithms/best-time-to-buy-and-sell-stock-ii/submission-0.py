class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        # if it goes from high to low should have already sold as it keeps going higher keep

        holding = prices[0]
        profit = 0
        prices += [0]
        for i in range(len(prices)-1):
            print(holding)
            if prices[i] > prices[i+1]:
                profit += prices[i] - holding
                holding = prices[i+1]
                print("profit",profit)
        return profit
            

        
        