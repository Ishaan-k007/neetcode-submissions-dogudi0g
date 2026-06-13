
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        


        # variable sized fixed size window 
        # what happens if I have K = 1 but an empty string?

        # 2 pointers L, R L starts at 0 start of window and R iterates through the string increasing the string size. the windows condition
        # is that at most there can be k + 1 unqiue letters inside.(To do this the max freq char has to have a count of R - k - 1) The moment this exceeds remove from left side to meet this condition.
        # store the size of the largest size window and return


        max_length = 0
        L = 0
      
        freq = {}
        


        for R in range(len(s)):
            
            count = freq.get(s[R], 0 ) + 1 
            freq[s[R]] = count
        
            max_count = max(freq.values())
            while (R - L + 1) - max_count > k:
                count = freq.get(s[L]) - 1
                freq[s[L]] = count
    
                L += 1
            max_length = max(max_length, R - L + 1)
        max_length = max(max_length,len(s) - L)
        return max_length





        