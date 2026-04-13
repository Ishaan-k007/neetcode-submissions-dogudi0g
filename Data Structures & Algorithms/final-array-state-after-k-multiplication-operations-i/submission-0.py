class Solution:
    def getFinalState(self, nums: List[int], k: int, multiplier: int) -> List[int]:

        heap = [(val, i) for i, val in enumerate(nums)]
        heapq.heapify(heap)

        for i in range(k):
            val, idx = heapq.heappop(heap)
            val = val * multiplier
            heapq.heappush(heap, (val, idx))
            nums[idx] = val
        return nums