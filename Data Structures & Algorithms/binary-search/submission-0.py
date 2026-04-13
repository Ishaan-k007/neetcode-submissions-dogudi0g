class Solution:
    def search(self, nums: List[int], target: int) -> int:
        L = 0
        R = len(nums) - 1

        while L <= R:
            mid_idx = (R + L) //2
            print(mid_idx)
            if nums[mid_idx] > target:
                R = mid_idx - 1
                print(nums[:R])
            elif nums[mid_idx] < target:
                L = mid_idx + 1
                print(nums[L:])
            else:
                return mid_idx
        return -1
        