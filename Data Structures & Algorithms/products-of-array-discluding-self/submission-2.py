class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:

        prefix_array = [0 for i in range(len(nums))]
        suffix_array = [0 for i in range(len(nums))]
        current_sum = 1
        
        result = [0 for i in range(len(nums))]
        for i in range(len(nums)):
            prefix_array[i] = current_sum
            current_sum = nums[i] * current_sum
        

        current_sum = 1
        for i in range(len(nums) -1 ,-1,-1):
            suffix_array[i] = current_sum
            current_sum = nums[i] * current_sum
        
        for i in range(len(nums)):
            result[i] = prefix_array[i] * suffix_array[i]
        return result






        


        
        