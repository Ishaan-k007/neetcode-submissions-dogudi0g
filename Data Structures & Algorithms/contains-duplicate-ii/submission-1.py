class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        R = 0
        L = 0
        window = set()
        while R < len(nums):
            
            if len(window) > k:
                window.remove(nums[L])
                L += 1
            if nums[R] in window:
                print(window)
                return True
            window.add(nums[R])
            R += 1
        return False

        