class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        upper_bound = max(piles)
        lower_bound = 1
       
       

        while lower_bound < upper_bound:
            middle = (upper_bound + lower_bound) // 2
            count = 0

            for pile in piles:
                count += math.ceil(float(pile) / middle)


            if count > h:
                lower_bound = middle + 1
            else:
                upper_bound = middle 
            
        return lower_bound 


        