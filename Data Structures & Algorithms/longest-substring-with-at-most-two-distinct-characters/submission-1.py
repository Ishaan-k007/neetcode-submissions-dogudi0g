class Solution:
    def lengthOfLongestSubstringTwoDistinct(self, s: str) -> int:
        # keep inc window till set length > 2
        # then keep decreasing from left

        L = 0
        max_length = 0
        seen = set()
        freq = {}
        for R in range(len(s)):

            seen.add(s[R])
            freq[s[R]] = freq.get(s[R], 0) + 1
            while len(seen) > 2:
                freq[s[L]] = freq[s[L]] - 1
                if freq[s[L]] == 0:
                    del freq[s[L]]
                    seen.remove(s[L])
                L += 1
            max_length = max(max_length , R - L + 1)

        return max_length 

            


        