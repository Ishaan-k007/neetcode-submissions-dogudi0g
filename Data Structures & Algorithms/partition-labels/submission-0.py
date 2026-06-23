class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        cur_end = 0
        last_index_map = {}
        count = 1
        res = []

        for i in range(len(s)):
            last_index_map[s[i]] = i
        

        for i in range(len(s)):
            temp = last_index_map.get(s[i])
            cur_end = max(cur_end,temp)
            if i == cur_end:
                res.append(count)
                count = 0
                cur_end = temp
            count += 1
        
        return res