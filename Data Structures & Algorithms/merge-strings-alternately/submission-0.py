class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        l = 0
        r = 0
        output_str = str()
        min_count = min(len(word1),len(word2))
        for i in range(min_count):
            output_str += word1[l]
            output_str += word2[r]
            l += 1
            r += 1
        output_str += word1[l:len(word1)]
        output_str += word2[r:len(word2)]

        return output_str

