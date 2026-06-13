class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        
        # convert to set for O(1)
        # find the start of sequences by seeing if there is num - 1 in list
        # keep looking for num + 1 
        # longest sequence returns
        
        numSet = set(nums)
        longest = 0
        for i in range(len(nums)):
            if (nums[i] - 1) not in numSet:
                length = 1
                while (nums[i] + length) in numSet:
                    length += 1
                longest = max(length, longest)
        return longest
            
            

        

        


                
        


        

       
       

                
                

        