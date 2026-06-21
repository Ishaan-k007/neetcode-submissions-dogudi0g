class Solution:
    def rob(self, nums: List[int]) -> int:
        #rob1 = best total from two houses ago
        #rob2 = best total from previous house
        
        rob1, rob2 = 0, 0

        # rob1,rob2,n,n+1
        for n in nums:
            # choosing whether to rob current house or skip
            temp = max(n + rob1, rob2)
            #update rob1 so now it is the value of the best total from 2 houses ago for the next iteration
            rob1 = rob2
            # update the total so it has the value of the prev best total when you move on to the next iteration
            rob2 = temp
        return rob2
        