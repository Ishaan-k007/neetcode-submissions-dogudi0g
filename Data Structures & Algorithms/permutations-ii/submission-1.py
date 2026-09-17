class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:

        
        res = []
        path = []
        used = set()
        nums.sort()
        def dfs():
            if len(path) == len(nums):
                res.append(path[:])
                return

            for i in range(len(nums)):

                if i in used:
                    continue
                
                if i > 0 and nums[i] == nums[i - 1] and (i - 1) not in used:
                    continue

                used.add(i)
                path.append(nums[i])

                dfs()

                path.pop()
                used.remove(i)

        dfs()
        return res
                    



        