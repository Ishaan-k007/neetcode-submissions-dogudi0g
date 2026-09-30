class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:

        freq = Counter(tasks)
        
        heap = []

        for key, value in freq.items():
            heapq.heappush(heap, (-value,key))
        
        # max heap containing tasks

        cooldown = deque()
        res = 0

        while heap or cooldown:
            if heap == []:
                res += 1
            else:
                
                cur_value, cur_task = heapq.heappop(heap)
                cur_value = -cur_value
                res += 1
                cur_value -= 1
                if cur_value != 0:
                    cooldown.append((cur_value,cur_task,res+n))
            
            if cooldown:
                cur_value , cur_task, cool_down_end = cooldown[0]
                if res == cool_down_end:
                    cooldown.popleft()
                    heapq.heappush(heap,(-cur_value,cur_task))
        
        return res
            
        