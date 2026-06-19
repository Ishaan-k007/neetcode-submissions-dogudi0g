class Solution:
    def climbStairs(self, n: int) -> int:
        memo = {}
        def dfs(i):
            if i <= 2: return i
            if i not in memo:
                memo[i] = dfs(i - 1) + dfs(i - 2)
            return memo[i]
              
        total = dfs(n)
        return total