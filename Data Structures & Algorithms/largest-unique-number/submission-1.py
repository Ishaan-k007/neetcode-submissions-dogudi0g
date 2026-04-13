class Solution:
    def largestUniqueNumber(self, nums: List[int]) -> int:
        num_map = {}

        for i in range(len(nums)):
            count = num_map.get(nums[i],0)
            num_map[nums[i]] = count + 1

        max_number = -1

        for key, value in num_map.items():
            if value == 1:
                max_number = max(key, max_number)

        return max_number 


        
        