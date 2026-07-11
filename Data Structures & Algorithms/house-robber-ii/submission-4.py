class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        memo = {}
        def dfs(i, flag):
            if i >= len(nums) or (flag and i == len(nums) - 1):
                return 0
            
            state = (i, flag)
            if state in memo:
                return memo[state]

            memo[state] = max(dfs(i + 1, flag),
                       nums[i] + dfs(i + 2, flag or i == 0))
            return memo[state]
        return max(dfs(0, False), dfs(1, False))