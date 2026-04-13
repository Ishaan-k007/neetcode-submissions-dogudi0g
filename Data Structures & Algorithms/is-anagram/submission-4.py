class Solution:
    #overall logic - anagram contains same amount of different letters e.g.
    # a=3, b=2, c =2 so hashmaps are the same
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) == len(t): #make sure they are the same length
            s_hashmap = {}
            t_hashmap = {}
            for i in range(len(s)):
                s_hashmap[s[i]]  = 1 + s_hashmap.get(s[i],0) #this line searches the map for the s[i] key. If it finds it, it adds one on to the value. If not it creates a new key key with a default value of 0
                t_hashmap[t[i]]  = 1 + t_hashmap.get(t[i],0)
            return s_hashmap == t_hashmap    # if hashmaps are = then anagram
        return False 