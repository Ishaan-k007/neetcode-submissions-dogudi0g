class Solution:
    def findMaxForm(self, strs: List[str], m: int, n: int) -> int:
        
        memo = {}
        def dp(i,m,n):
            if i == len(strs):
                return 0

            if (i,m,n) in memo:
                return memo[(i,m,n)]

            # Don't include item i
            skip =  dp(i + 1, m,n)

            # Include item i
            zeros = strs[i].count("0")
            ones = strs[i].count("1")
            take = 0
            if zeros <= m and ones <= n:


            
                take = 1 + dp(i + 1, m - zeros,n - ones)
            memo[(i,m,n)] = max(skip, take)
            return memo[(i, m, n)]
        return dp(0,m,n)