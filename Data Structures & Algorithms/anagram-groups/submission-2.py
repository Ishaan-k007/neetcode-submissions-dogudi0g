
from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        anagrams = defaultdict(list)
        result = []
        for word in strs:
            key = "".join(sorted(word))
            anagrams[key].append(word)


        for value in anagrams.values():
            result.append(value)

        return result 

        


            

        
        
