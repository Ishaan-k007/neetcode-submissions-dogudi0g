class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:

        index_map = {}
        for i in range(len(numbers)):
            index_map[numbers[i]] = i

        for i in range(len(numbers)):
            difference = target - numbers[i]
            if difference in numbers:
                second_index = index_map.get(difference)
                return [i + 1,second_index + 1]





        


        