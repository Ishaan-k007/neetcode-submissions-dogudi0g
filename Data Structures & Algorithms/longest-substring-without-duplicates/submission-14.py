class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:


        # variable size sliding window

        L = 0 
        max_length = 0
        window = set()
        for i in range(len(s)):
            
            
            while s[i] in window:
                window.remove(s[L])
                L += 1
        
            window.add(s[i])
            max_length = max(max_length, i - L + 1)
        
        return max_length 
            

                

        