from collections import Counter
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        size_of_window = len(s1)
        
        if size_of_window == 1:
            if s1 in s2:
                return True
            else:
                return False
        L = 0
        cur_str = ""
        s1_map = Counter(s1)


        for R in range(len(s2)):
            cur_str += s2[R]

            if R - L + 1 == size_of_window:
                cur_map = Counter(cur_str)

                if cur_map == s1_map:
                    return True
                else:
                    cur_str = cur_str[1:]
                  
                    L += 1
        return False
