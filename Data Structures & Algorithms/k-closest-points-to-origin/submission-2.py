import math
from collections import defaultdict
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:


       ## heap implementation:
       ## create a heap (distance) 

        distance_map =defaultdict(list)
        min_heap = []
        for point in points:
            distance = point[0] * point[0] + point[1] * point[1]
            distance_map[distance].append(point)
            min_heap.append(distance)
        heapq.heapify(min_heap)
        res = []
        for i in range(k):
            distance = heapq.heappop(min_heap)
            res.append(distance_map[distance].pop())

        return res
