class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:

        low = max(weights)
        high = sum(weights)

        def number_of_days_required(capacity):

            current_weight = 0
            days_req = 1
            
            for weight in weights:
                
                if current_weight + weight > capacity:
                    days_req += 1
                    current_weight = 0
                current_weight += weight
                
            return days_req
             

        while low < high:
            mid = (low+high) // 2

            
            if number_of_days_required(mid) > days:
                low = mid + 1 
            if number_of_days_required(mid) <= days:
                high = mid
        

        return low

        