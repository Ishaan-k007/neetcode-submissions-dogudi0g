class Solution:
    def firstUniqChar(self, s: str) -> int:
        count_map = {}

        # Count occurrences of each character
        for ch in s:
            count_map[ch] = count_map.get(ch, 0) + 1

        # Find index of first char with count == 1
        for i, ch in enumerate(s):
            if count_map[ch] == 1:
                return i

        return -1  # if no unique character found
