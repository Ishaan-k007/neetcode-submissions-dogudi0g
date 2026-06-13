from collections import defaultdict
from collections import Counter

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        result = []
        freq = defaultdict(int)
        freq = Counter(nums)

        sorted_freq = dict(sorted(freq.items(), key=lambda x: x[1], reverse = True))

        i = 0
        for key in sorted_freq:
            if i == k:
                break
            result.append(key)
            i += 1

        return result





