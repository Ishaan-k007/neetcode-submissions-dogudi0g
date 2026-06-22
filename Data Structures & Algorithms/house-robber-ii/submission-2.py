class Solution:
    def rob(self, nums: List[int]) -> int:
        #rob1 = best total from two houses ago
        #rob2 = best total from previous house
        
        rob1, rob2 = 0, 0
        
        if len(nums) == 1:
            return nums[0]

        # rob1,rob2,n,n+1
        for n in nums[1:]:
            # choosing whether to rob current house or skip
            temp = max(n + rob1, rob2)
            #update rob1 so now it is the value of the best total from 2 houses ago for the next iteration
            rob1 = rob2
            # update the total so it has the value of the prev best total when you move on to the next iteration
            rob2 = temp
        rob3 = 0
        rob4 = 0
        for n in nums[:len(nums)-1]:
            # choosing whether to rob current house or skip
            temp = max(n + rob3, rob4)
            #update rob1 so now it is the value of the best total from 2 houses ago for the next iteration
            rob3 = rob4
            # update the total so it has the value of the prev best total when you move on to the next iteration
            rob4 = temp
        
        
        
        
        
        return max(rob2,rob4)
