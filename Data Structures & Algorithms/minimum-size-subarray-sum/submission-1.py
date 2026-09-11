class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:

        # sliding window
        # increase the window untill window sum greater than or equal to the target
        # decrease when greater track each window size returning smallest


        # O(n)

        # target = 10, nums = [2,1,5,1,5,3]
        # cur_sum = 2, 3, 8, 9, 14  min_size = 5
        # 12 min_size = 4
        # 11 min_size = 3
        # 6 

        L = 0
        cur_sum = 0
        min_size = float("inf")
        for R in range(len(nums)):
            cur_sum += nums[R]

            while cur_sum >= target:
                min_size = min(min_size,R - L + 1)
                cur_sum -= nums[L]
                L += 1
        if min_size == float("inf"):
            return 0
        return min_size

                    