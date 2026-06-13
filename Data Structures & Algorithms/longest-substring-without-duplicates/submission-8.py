class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:



        # sliding window variable sized problem
        # what happens empty string / one letter string?
        # start at L = 0 and then increase R (thw window) till R hits a repeatted character in the window
        # then move L till the window only contains unique letters , then repeat till end of array
        # keep track of max_length window and return this

        max_length = 0
        cur_length = 0
        window = set()

        L = 0

        for R in range(len(s)):
            
            if s[R] not in window: 
                window.add(s[R])
            else:
                cur_length = R - L
                max_length = max(max_length,cur_length) 
                while s[R] in window:
                    window.remove(s[L])
                    L += 1
                window.add(s[R])
        
        cur_length = len(s) - L
        return max(max_length,cur_length)

            



        
