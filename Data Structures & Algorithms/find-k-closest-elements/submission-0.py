import heapq
class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:


        # populate another array with diff
        
        diff = []

        for i in range(len(arr)):
            diff.append(abs(arr[i] - x))

        heap = [(diff[i], i) for i in range(len(diff))]
        heapq.heapify(heap)

        res = []
        for i in range(k):
            value, index = heapq.heappop(heap)
            res.append(arr[index])

        res.sort()
        return res
            



        