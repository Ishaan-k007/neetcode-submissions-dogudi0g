class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        
        stones = [-stone for stone in stones]
        heapq.heapify(stones)

        while len(stones) > 1:
            first_stone = -heapq.heappop(stones)
            second_stone = -heapq.heappop(stones)

            if first_stone > second_stone:
                first_stone = first_stone - second_stone
                heapq.heappush(stones , -first_stone)
            
        if len(stones) == 1:
            return -stones[0]
        else:
            return 0
