class Solution:
    def validWordAbbreviation(self, word: str, abbr: str) -> bool:
        l = 0  # pointer for abbr
        r = 0  # pointer for word

        while l < len(abbr):
            if abbr[l].isalpha():
                # Must match current word letter
                if r >= len(word) or abbr[l] != word[r]:
                    return False
                l += 1
                r += 1
            elif abbr[l].isdigit():
                if abbr[l] == '0':
                    return False  # Leading zeros not allowed
                num = 0
                while l < len(abbr) and abbr[l].isdigit():
                    num = num * 10 + int(abbr[l])
                    l += 1
                r += num  # skip characters in word
            else:
                return False  # Invalid character

        return r == len(word)  # We must consume the entire word


        if r == len(word) - 1:
            return True
        return False

            