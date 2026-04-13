class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        longest_sequence = 0 
        l = 0
        r = 0
        num_zeros = 0

        for r in range(len(nums)):
            if nums[r] == 0:
                num_zeros += 1

            while num_zeros > 1:
                if nums[l] == 0:
                    num_zeros -= 1
                l += 1

            longest_sequence = max(longest_sequence,r-l + 1)

        return longest_sequence 