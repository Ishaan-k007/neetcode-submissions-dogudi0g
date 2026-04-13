
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        L = 0
        result = 0
        char = {}
        
        for R, ch in enumerate(s):
            char[ch] = char.get(ch,0) + 1
            max_frequency = max(char.values())
            while R-L + 1 - max_frequency > k:
                char[s[L]] -= 1
                L += 1
            
            result = max(result,R-L + 1) 
        return result 

        