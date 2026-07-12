class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:

        memo = {}
        def solve(index, prev_index):
            if index == len(nums):
                return 0
            # Option 1: Exclude nums[index]
            state = (index,prev_index)
            if state in memo:
                return memo[state]
             
            res = solve(index + 1, prev_index)
            
            # Option 2: Include nums[index] (if valid)
            if prev_index == -1 or nums[index] > nums[prev_index]:
                res = max(res, 1 + solve(index + 1, index))
            
            memo[state] = res
            
            return memo[state]
        return solve(0,-1)