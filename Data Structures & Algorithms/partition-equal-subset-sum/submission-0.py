class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        if sum(nums) % 2 != 0:
            return False
        
        target = sum(nums) // 2

        def recurse(curSum,index):
            if curSum > target or index == len(nums):
                return False
            if curSum == target:
                return True
            return recurse(curSum + nums[index], index +1) or recurse(curSum,index + 1)
        return recurse(0,0)



        