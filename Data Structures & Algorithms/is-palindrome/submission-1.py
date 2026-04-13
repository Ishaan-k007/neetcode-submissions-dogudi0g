class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = re.sub(r'[^A-Za-z0-9]', '', s)
        s = s.lower()
        print(s)
        l = 0
        r = len(s) - 1
        res = True
        while l < r:
            if s[l] != s[r]:
                res = False
                break
            l += 1
            r -= 1

        return res
        