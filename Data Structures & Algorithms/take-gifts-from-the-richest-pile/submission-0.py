import math
class Solution:
    def pickGifts(self, gifts: List[int], k: int) -> int:

        ## python only has min heap so heappop gives min element
        gifts = [-g for g in gifts]
        heapq.heapify(gifts)


        for i in range(k):
            
            temp = -heapq.heappop(gifts) #because they are negative convert to pos to sqrt 
            temp = math.isqrt(temp)   # integer sqrt
            heapq.heappush(gifts, -temp)
        print(gifts)
        return abs(sum(gifts)) 

        