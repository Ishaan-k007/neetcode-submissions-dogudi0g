class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        # the last cap 
        
        def helper(cap,weights,days):
            cur_sum = 0
            cur_days = 0
            for i in range(len(weights)):
                if cur_sum + weights[i] > cap:
                    cur_sum = weights[i]
                    cur_days += 1
                else:
                    cur_sum += weights[i]
            cur_days += 1        
            if cur_days  <= days:
                return True
            return False

        
        
        low_cap = max(weights)
        high_cap = sum(weights)


        while low_cap < high_cap:
            mid = (low_cap + high_cap) // 2

            if helper(mid,weights,days):
                high_cap = mid
            else:
                low_cap = mid + 1
        return low_cap
