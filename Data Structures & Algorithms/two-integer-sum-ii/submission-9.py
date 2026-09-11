class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        prev_idx = {}
        res = []
        for i in range(len(numbers)):
            if target - numbers[i] in prev_idx:
                res.append(prev_idx[target - numbers[i]] + 1)
                res.append(i  + 1)
                
                return res
            prev_idx[numbers[i]] = i
        
            
        