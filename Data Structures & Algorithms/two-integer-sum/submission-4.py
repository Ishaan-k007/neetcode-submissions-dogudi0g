class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        index_map = {}
        result = []

        for i in range(len(nums)):
            difference = target - nums[i]

            if difference in index_map:
                
                result.append(index_map[difference])
                result.append(i)
            
            index_map[nums[i]] = i
        return result


        
        

            