class Solution:
    def characterReplacement(self, s: str, k: int) -> int:

        # VARIABLE SLIDING WINDOW LEN k

        L = 0
        window = {}
        max_window_size = 0
        for i in range(len(s)):
            window[s[i]] = window.get(s[i],0) + 1
            if window:
                while (i - L +1) - max(window.values()) > k:
                    window[s[L]] = window.get(s[L],0) - 1
                    if window[s[L]] == 0:
                        del window[s[L]]
                    L += 1
                
            
            max_window_size = max(max_window_size , i - L + 1)

        return max_window_size
        