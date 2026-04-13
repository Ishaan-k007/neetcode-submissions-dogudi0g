class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        
        # append the task and its frequency to a hash_map called count map
        count_map = Counter(tasks)
        maxHeap = []
        # append the frequency of the task to a heap: Remember as it is a max heap append the negative 
        # heap dont care about the task only the frequency 
        for count in count_map.values():
            maxHeap.append(-count)
        heapq.heapify(maxHeap)
        
        time = 0

        # while there is items in the heap or the queue
        # pop the most frequent item in the heap
        # because heap is negative add 1 to the count (this has the effect of -1 to the count)
        # set up a queue with the new count and the time when the cooldown ends (time + n)
        # if there is nothing in map then set time to the first time in the queue 
        # if the time = the first item in the queues time then can push the count back into the heap

        queue = deque()
        
        while queue or maxHeap:
            time += 1
            if maxHeap:
                
                freq = 1 + heapq.heappop(maxHeap)
                if freq:
                    queue.append([freq, time + n]) # queue can only append one item wrap this in a tuple or list
            else:
                time = queue[0][1]
            
            if queue and queue[0][1] == time:
                heapq.heappush(maxHeap, queue.popleft()[0])
        return time





        
        