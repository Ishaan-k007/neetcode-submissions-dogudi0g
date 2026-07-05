class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        
        res = []
      
        candidates.sort()
        def backtrack(subset,remaining_target,i):

            if remaining_target == 0:
                

                res.append(subset[:])
                return 

            if remaining_target < 0:
                return

            for j in range(i,len(candidates)):
                if j > i and candidates[j] == candidates[j - 1]:
                    continue
                subset.append(candidates[j])
                remaining_target -= candidates[j]
                backtrack(subset, remaining_target, j+1)

                subset.pop()
                remaining_target += candidates[j]
        backtrack([],target,0)
        return res
                 
