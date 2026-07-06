class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:

        memo = {}
        def dfs(i):
            if i in memo:
                return memo[i]
            if i == len(s):
                return True
            
            cur_str = ""
            for j in range(i,len(s)):
                cur_str += s[j]
                if cur_str in wordDict:
                    if dfs(j+1):
                        memo[i] = True
                        return True
            
            memo[i] = False
            return False
        return dfs(0)