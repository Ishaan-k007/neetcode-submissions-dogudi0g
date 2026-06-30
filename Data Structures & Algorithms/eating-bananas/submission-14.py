class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        L = 1
        R = max(piles)

        while L <= R:
            cur_hours = 0
            mid = (L + R) // 2

            for pile in piles:
                cur_hours += math.ceil(pile / mid)

            if cur_hours <= h:
                R = mid - 1
            else:
                L = mid + 1

        return L
      

        