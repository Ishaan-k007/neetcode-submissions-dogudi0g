class Solution:
    def maxArea(self, heights: List[int]) -> int:

        # 2 pointer one at start one at end move according to whichever has the lower height

        L = 0
        R = len(heights) - 1
        max_area = 0
        cur_area = 0
        while L < R:
            cur_area = min(heights[L],heights[R]) * (R - L)
            max_area = max(max_area,cur_area)

            if heights[L] < heights[R]:
                L += 1
            else:
                R -= 1

        return max_area




        