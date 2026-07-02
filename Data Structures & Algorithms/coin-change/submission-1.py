class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        #the minimum coins needed to make every amount from 0 up to amount
        dp = [float("inf")] * (amount + 1)
        dp[0] = 0

        for a in range(1,amount+1):
            for coin in coins:
                if a - coin >= 0:
                    dp[a] = min(dp[a], 1+ dp[a-coin])

        if dp[amount] == float("inf"):
            return -1
        else:
            return dp[amount
            ] 

        