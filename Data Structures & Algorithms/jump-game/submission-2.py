class Solution:
    def canJump(self, nums: List[int]) -> bool:

        goal = len(nums) - 1

        for i in range(len(nums) - 1,-1,-1):
            # if i + jump can reach the goal then can update the goal to i
            if i + nums[i] >= goal:
                goal = i
        if goal == 0:
            return True
        else:
            return False
