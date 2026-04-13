class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        
        res = []
        def backtrack(i,subset,target):
            nonlocal res 

            if sum(subset) == target:
                res.append(subset[:])
                return
            
            if sum(subset) > target:
                return

            for j in range(i,len(nums)):
                subset.append(nums[j])
                backtrack(j,subset,target)
                subset.pop()
               
            
        backtrack(0,[],target)
        return res