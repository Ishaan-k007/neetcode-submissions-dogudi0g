class Solution:
    def arrangeCoins(self, n: int) -> int:


        if n == 0:
            return 0

        count = 1
        while n > 0:
            n -= count
            count += 1 

        if n < 0:
            count -= 1
        
        return count - 1 