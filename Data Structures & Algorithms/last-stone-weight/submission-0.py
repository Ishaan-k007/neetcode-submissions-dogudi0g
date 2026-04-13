class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        """ heap pop will remove the first element of the array. Python only 
        has min heaps so to remove the largest element we append the negative of the element """

        stones =  [-s for s in stones]
        heapq.heapify(stones)

        while len(stones) > 1:
            first = heapq.heappop(stones)
            second = heapq.heappop(stones)

            if second > first:
                heapq.heappush(stones, first - second)
        stones.append(0)
        return abs(stones[0])

            
        
        