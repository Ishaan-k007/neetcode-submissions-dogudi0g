
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:

        # variable size sliding window
        # keep increasing the window size for a new letter if it has been seen before increase count
        # if size of window - max_frequent char > k  then store size of window and decide if it is greater than current window size
            # decrement the window from the left untill this constraint is satisfied 
        # return max size
        # Aiming for O(n) Time and space

        # 
        max_frequency = 0
        freq = {}
        L = 0
        res = 0
        for R in range(len(s)):
            frequency = freq.get(s[R],0) + 1
            freq[s[R]] = frequency
            max_frequency = max(max_frequency,frequency)

            while R - L + 1 - max_frequency > k:
                freq[s[L]] -= 1
                L += 1
            res = max(res , R - L + 1)
        return res



       
        # seen = ("X")
        # seen = ("X")
                    
                


        





        