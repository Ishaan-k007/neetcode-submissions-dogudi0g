class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        
        # Use a binary search from k =0 to k = max(in array) to determine first k that satifies target = LOWER BOUND
        # Need to calculate whether the k is acceptable or not:
            # Do this using for loop doing floor division until 0  

        L = 1
        R = max(piles)

        while L < R:
            count = 0
            mid = (L + R ) // 2

            for i in range(len(piles)):
                count += math.ceil(piles[i] / mid)

            if count > h:
                L = mid + 1

            else:
                R = mid


        return L