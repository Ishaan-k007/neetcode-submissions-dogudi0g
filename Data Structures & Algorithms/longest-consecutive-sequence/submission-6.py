class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:

        # need to find start consecutive elements elements such that i + 1 exists but i -1 doesnt exist 
        # for each start element find consecutive sequence
        if len(nums) == 0:
            return 0
        start = []
        for i in range(len(nums)):
            if nums[i] + 1 in nums:
                if nums[i] - 1 not in nums:
                    start.append(nums[i])

        max_count = 1
        for value in start:
            current_count = 0
            while value in nums:
                value = value + 1
                current_count += 1
            
            max_count = max(max_count,current_count)
        return max_count


                
        


        

       
       

                
                

        