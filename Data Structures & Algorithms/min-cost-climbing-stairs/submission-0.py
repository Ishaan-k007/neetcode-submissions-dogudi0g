class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:

        cache = [-1] * len(cost)

        cache[len(cost) - 1] = cost[len(cost) - 1]
        cache[len(cost) - 2] = cost[len(cost) - 2]

        for i in range(len(cost) - 3, -1, -1):
            cache[i] = min(cache[i + 1], cache[i+2]) + cost[i]
        
        return min(cache[0],cache[1])


        