class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        L = 0
        R = 1

        while L < (len(nums) - 1):
            R = L + 1
            for i in range(R,len(nums)):
                

                if nums[R] < nums[L]:
                    temp = nums[R]
                    nums[R] = nums[L]
                    nums[L] = temp
                R += 1
            L += 1
        return nums
            



        