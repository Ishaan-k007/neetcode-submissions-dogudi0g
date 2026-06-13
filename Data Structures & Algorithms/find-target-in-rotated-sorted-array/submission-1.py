class Solution:
    def search(self, nums: List[int], target: int) -> int:

        # find pivot index 

        L = 0
        R = len(nums) - 1

        while L < R:
            mid = (L + R) // 2
            if nums[mid] > nums[R]:
                L = mid + 1
            else:
                R = mid

        if nums[L] == target:
            return L
        # preform binary search on both segments

        def binary_search(L,R,target):

            while L <= R:
                mid = (L + R) // 2

                if nums[mid] == target:
                    return mid

                elif nums[mid] < target:
                    L = mid + 1
                else:
                    R = mid - 1
            return -1

        count = binary_search(0,L,target)
        count = max(count, binary_search(L,len(nums) - 1, target))
        return count






        
        