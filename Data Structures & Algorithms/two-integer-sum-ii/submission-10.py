class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        L = 0
        R = len(numbers) - 1
        res = []
        while L < R:
            cur_sum = numbers[L] + numbers[R]

            if cur_sum == target:
                res.append(L + 1)
                res.append(R + 1)
                return res 
            elif cur_sum < target:
                L += 1

            else:
                R -= 1
        
            
        