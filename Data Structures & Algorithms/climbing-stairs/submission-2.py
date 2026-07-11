class Solution:
    def climbStairs(self, n: int) -> int:
        
        
        memo = {}
        def dfs(x):

            if x == n:
                return 1
            if x > n:
                return 0
            
            if x in memo:
                return memo[x]
            
            memo[x] = dfs(x + 1) + dfs(x+2)
            return memo[x]
        return dfs(0)

            