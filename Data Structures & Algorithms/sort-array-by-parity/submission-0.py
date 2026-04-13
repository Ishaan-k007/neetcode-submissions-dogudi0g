class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        L = 0
        R = 0

        while R < len(nums):
            if nums[R] % 2 == 0:
                temp = nums[L]
                nums[L] = nums[R]
                nums[R] = temp
                L += 1
            R += 1
        return nums
             

            

        