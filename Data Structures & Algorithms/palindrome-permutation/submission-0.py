class Solution:
    def canPermutePalindrome(self, s: str) -> bool:
        letter_map = {}
        overall_count = 0
        for i in range(len(s)):
            count = letter_map.get(s[i],0)
            letter_map[s[i]] = count + 1
        
        for value in letter_map.values():
            if value % 2 != 0:
                overall_count += 1

        if overall_count <= 1:
            return True
        else:
            return False 


            


        