class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        L = 0
        R = len(s1) - 1
   
        def mapping(s):
            s_map = {}
            for i in range(len(s)):
                if s[i] in s_map:
                    s_map[s[i]] += 1
                else:
                    s_map[s[i]] = 1
            return s_map

        s1_map = mapping(s1)
        s2_map = mapping(s2[L:R+1])

        while R < len(s2):

            if s2_map == s1_map:
                return True
            
            s2_map[s2[L]] -= 1
            if s2_map[s2[L]] == 0:   # cleanup
                del s2_map[s2[L]]
            L+= 1
            R += 1
            if R == len(s2):
                return False
            s2_map[s2[R]] = s2_map.get(s2[R],0) + 1
        return False


        
            
            