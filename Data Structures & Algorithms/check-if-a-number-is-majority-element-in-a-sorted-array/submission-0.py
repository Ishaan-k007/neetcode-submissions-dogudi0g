class Solution:
    def isMajorityElement(self, nums: List[int], target: int) -> bool:
        count = 0
        if target in nums:
            for i in range(len(nums)):
                if nums[i] == target:
                    count += 1
        
        else:
            return False


        if count > len(nums) / 2:
            return True
        else:
            return False
            


        