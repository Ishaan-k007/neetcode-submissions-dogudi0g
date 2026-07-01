from collections import defaultdict
from collections import Counter

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        freq_map = Counter(nums)

        top_k_keys = sorted(freq_map, key=freq_map.get, reverse=True)[:k]
        return top_k_keys 
                        
        
        





