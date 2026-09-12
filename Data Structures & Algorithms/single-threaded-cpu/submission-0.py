import heapq
class Solution:
    def getOrder(self, tasks: List[List[int]]) -> List[int]:

        # heap
        # as the enqueue time keeps progressing keep adding to the heap
        # add the processing time and the index
        # each time pop the smallest proccessing time if multiple then smallest index
        # append this to a res array

        for i, t in enumerate(tasks):
            t.append(i)
        tasks.sort(key=lambda t: t[0])

        res = []
        minHeap = []
        i = 0
        time = tasks[0][0]

        while minHeap or i < len(tasks):
            while i < len(tasks) and time >= tasks[i][0]:
                heapq.heappush(minHeap, [tasks[i][1], tasks[i][2]])
                i += 1
            if not minHeap:
                time = tasks[i][0]
            else:
                procTime , index = heapq.heappop(minHeap)
                time += procTime
                res.append(index)
        return res
            


        

        