class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        set_num = set(nums)
        if len(set_num) == len(nums):
            return False
        else:
            return True
        
         