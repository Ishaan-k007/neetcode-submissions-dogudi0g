class Solution:
    def minimumDifference(self, nums: List[int], k: int) -> int:
        L = 0
        R = 0
        overall_min_dif = 9999
        current_min_dif = 99999
        nums = sorted(nums)
        temp_arr = []
     

        while R < len(nums):
            temp_arr.append(nums[R])
            if R - L +1 == k: 
                
                print(temp_arr)
                current_min_dif = max(temp_arr) - min(temp_arr)
                overall_min_dif = min(overall_min_dif,current_min_dif)
                
                temp_arr.remove(nums[L])
                L += 1
           
            R += 1
            
        return overall_min_dif


        