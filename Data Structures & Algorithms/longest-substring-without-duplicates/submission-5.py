class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        l = 0
        r = 0
        max_count = 0
        cur_str = []
        count = 0
        

        
        for r in range(len(s)):
            if s[r] in cur_str:
                count += 1

            cur_str.append(s[r])


            while count > 0:
                if s[l] == s[r]:
                    count -= 1
                cur_str.remove(s[l])
                l += 1
            max_count = max(max_count,r-l+1)
        return max_count
