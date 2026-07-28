from collections import Counter
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:

        # fixed window size s1 
        # go through s2 check if window is palindrome
        def is_permute(L,R):
            char_s2 = Counter(s2[L:R+1])
            if char_s1 == char_s2:
                return True
            return False
        char_s1 = Counter(s1)
        length_s1 = len(s1)
        L = 0
        for R in range(len(s2)):
            
            if R - L + 1 == length_s1:
                if is_permute(L,R):
                    return True
                L += 1
        return False

        

        
        
