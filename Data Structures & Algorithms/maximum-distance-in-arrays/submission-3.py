class Solution:
    def maxDistance(self, arrays: List[List[int]]) -> int:

        arrays = sorted(arrays)
        print(arrays)
        max_distance = 0
        for i in range(len(arrays)):
            for j in range(i+1,len(arrays)):
                max_distance = max(max_distance,abs(arrays[i][0] - arrays[j][-1]))
                max_distance = max(max_distance,abs(arrays[i][-1] - arrays[j][0]))
        return max_distance

        