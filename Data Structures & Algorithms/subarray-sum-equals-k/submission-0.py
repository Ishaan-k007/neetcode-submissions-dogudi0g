class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:


        # sliding window sol 
        # expand the window untill the sum >= k
        # if equal to k increment count
        # decrease the size of the window untill the sum is less than count
        # return count

        # [2,-1,1,2], k = 2
        # sum = 2 res = 1 sum = 0
        # sum = -1
        # sum = 0
        # sum = 2     res  = 2

        prefix_map = {0 : 1}

        count = 0
        res = 0
        for i in range(len(nums)):
            count += nums[i]
            if count - k in prefix_map:
                res += prefix_map[count - k]
            
            tmp = prefix_map.get(count,0) + 1
            prefix_map[count] = tmp
        return res



        