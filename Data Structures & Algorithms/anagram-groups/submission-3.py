from collections import Counter 
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # dict stores {c:3,a:2} = string input 
        # counting all the characters and storing char to num_times_appear in a dictionary
        # for every string in the array if it is already in the dict

        
        freq_to_string = {}
        results = []
        for string in strs:
            values = tuple(sorted(Counter(string).items()))
            if values in freq_to_string:
                freq_to_string[values].append(string)
            else:
                freq_to_string[values] = [string]
        
        for value in freq_to_string.values():
            results.append(value)
        
        return results
        




        