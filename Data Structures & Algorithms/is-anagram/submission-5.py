class Solution:
    #overall logic - anagram contains same amount of different letters e.g.
    # a=3, b=2, c =2 so hashmaps are the same
    def isAnagram(self, s: str, t: str) -> bool:
        count_s = {}
        count_t = {}
        if len(s) != len(t):
            return False
        for i in range(len(s)):
            count_of_letter_in_s = count_s.get(s[i],0)
            count_s[s[i]] = count_of_letter_in_s + 1
            count_of_letter_in_t = count_t.get(t[i],0)
            count_t[t[i]] = count_of_letter_in_t + 1
        if count_s == count_t:
            return True
        else:
            return False
            