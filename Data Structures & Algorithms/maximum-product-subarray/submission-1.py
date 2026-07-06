class Solution:
    def maxProduct(self, nums: List[int]) -> int:

        cur_min = 1
        cur_max = 1
        
        res_max = nums[0]

        for i in range(len(nums)):
            temp = cur_max
            cur_max = max(cur_max * nums[i],nums[i])
            cur_max = max(cur_max,cur_min * nums[i])
            cur_min = min(cur_min * nums[i], nums[i])
            cur_min = min(cur_min,temp * nums[i])
            res_max = max(res_max,cur_max)
        return res_max


        