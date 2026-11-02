class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # we have a set of nums to remove any duplicates
        # we only start on numbers that there is no number which is -1 of it
        # we see which number has the max sequence

        nums_set = set(nums)

        max_count_seq = 0
        for i in range(len(nums)):
            cur_num = nums[i]
            if cur_num - 1 in nums_set:
                continue
            else:
                cur_count_seq = 1
                while cur_num + 1 in nums_set:
                    cur_count_seq += 1
                    cur_num = cur_num + 1
                max_count_seq = max(max_count_seq,cur_count_seq)
        
        return max_count_seq


        