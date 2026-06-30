class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        L = 1
        R = max(piles)
        
        if len(piles) > h:
            return -1
        while L <= R:
            cur_hours = 0
            mid = (L+R) // 2
            if mid == 0: break

            for i in range(len(piles)):
                cur_hours += math.ceil(piles[i] / mid)
            
            if cur_hours <= h:
                res = mid
                R = mid - 1
            else:
                L = mid + 1
                

        return res
        