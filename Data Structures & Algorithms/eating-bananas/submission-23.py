import math
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        # min eating rate = 1
        # max eating rate = max(piles)

        L = 1
        R = max(piles)

        while L < R:

            mid = (L + R) // 2
            hours_req = 0
            for pile in piles:
                hours_req += math.ceil(pile/mid)


            if hours_req <= h:
                R = mid
            else:
                L = mid + 1
        return L
