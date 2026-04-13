class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:

       # sort the array 
       
       # left with 2 values go right to left like 2 sum ii that sum to -nums[i]

        nums = sorted(nums)
        res = []
        visited = []
        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            
            L = i +1
            R = len(nums) - 1
            while L < R:
                if nums[L] + nums[R] > -nums[i]:
                    R -= 1

                elif nums[L] + nums[R] < -nums[i]:
                    L +=1
                else:
                    res.append([nums[i],nums[L],nums[R]])
                    L += 1
                    R -= 1
                    while L < R and nums[L] == nums[L-1]:
                        L += 1
            visited.append(nums[i])
        return res