class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        
        res = []
        def backtrack(subset):
            nonlocal res 

            if len(subset) == len(nums):
                res.append(subset[:])
                return

            for num in nums:
                if num in subset:
                    continue
                subset.append(num)
                backtrack(subset)
                subset.pop()
        
        backtrack([])
        return res

