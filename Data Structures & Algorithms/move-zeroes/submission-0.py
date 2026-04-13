class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        L = 0
        R = 0
        while R < len(nums):
            if nums[R] != 0:
                temp = nums[L]
                nums[L] = nums[R]
                nums[R] = temp
                L += 1
            R += 1
        return nums
                
        