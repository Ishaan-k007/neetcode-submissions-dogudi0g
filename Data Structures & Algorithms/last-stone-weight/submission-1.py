class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        """ heap pop will remove the first element of the array. Python only 
        has min heaps so to remove the largest element we append the negative of the element """

        stones = [-n for n in stones]
        heapq.heapify(stones)

        while len(stones) > 1:
            first_stone = -heapq.heappop(stones)
            second_stone = -heapq.heappop(stones)
            res_stone = first_stone - second_stone
            if res_stone > 0:
                heapq.heappush(stones, -res_stone)
        if len(stones) == 1:
            return -stones[0]
        else:
            return 0
