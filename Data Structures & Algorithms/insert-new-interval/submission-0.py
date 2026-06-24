class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        # insert interval into array 
        # return merged inetrvals
        intervals.append(newInterval)

        sortedIntervals = sorted(intervals , key = lambda x : x[0])
        merged = []

        for interval in sortedIntervals:
            if not merged or interval[0] > merged[-1][1]:
                merged.append(interval)
            else:
                merged[-1][1] = max(interval[1],merged[-1][1])
        return merged 
        