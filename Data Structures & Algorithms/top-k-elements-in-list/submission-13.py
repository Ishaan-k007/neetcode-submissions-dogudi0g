from collections import Counter 
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # dictionary to map each number to its frequency
        # sort the dictionary
        # for k times append the more frequent number to a results array

        num_to_freq = Counter(nums)

        sorted_items = sorted(num_to_freq.items(), key=lambda item: item[1])
        
        n = len(sorted_items) - 1
        results = []
        for i in range(k):
            results.append(sorted_items[n- i][0])
        return results 






        