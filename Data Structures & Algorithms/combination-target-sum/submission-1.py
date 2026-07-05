class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        
        # target = 3   1 1 1  1 2 1 
        res = []

        def backtrack(subset,remaining_target,i):
            nonlocal res

            if remaining_target == 0:
                res.append(subset[:])
                return
            if remaining_target < 0:
                return

            
            
            for j in range(i,len(nums)):
                
                subset.append(nums[j])
                remaining_target -= nums[j]
                 
                backtrack(subset,remaining_target,j)
                remaining_target += nums[j]
                subset.pop()
              
        backtrack([],target,0)
        return res            
