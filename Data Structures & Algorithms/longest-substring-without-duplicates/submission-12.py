class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        set_s = set()
        L = 0
        best = 0

        for i in range(len(s)):
            
            while s[i] in set_s:
                set_s.remove(s[L])
                L += 1
            set_s.add(s[i])
            
            best = max(best , i - L + 1)
        best = max(best , len(s)  - L)
        return best
        
       
