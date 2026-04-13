class Solution:
    def customSortString(self, order: str, s: str) -> str:
        output = ""
        output_2 = ""
        s_map = {}
        for i in range(len(s)):
            if s[i] in s_map:
                s_map[s[i]] += 1
            else:
                s_map[s[i]] = 1
            if s[i] not in order:
                output_2 += s[i] 
        for i in range(len(order)):
            if order[i] in s:
                output += (order[i] * s_map[order[i]])
        
            
        return output + output_2

        