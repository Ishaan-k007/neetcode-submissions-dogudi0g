from typing import List

class Solution:
    def encode(self, strs: List[str]) -> str:
        # Format: "<length>#<word>"
        encrypted_string = ""
        for word in strs:
            encrypted_string += str(len(word)) + "#" + word
        return encrypted_string

    def decode(self, s: str) -> List[str]:
        output_array = []
        i = 0
        while i < len(s):
            # Find where the length ends (before the '#')
            j = i
            while s[j] != "#":
                j += 1
            length = int(s[i:j])  # parse the number
            word = s[j+1:j+1+length]
            output_array.append(word)
            i = j+1+length  # move to the next encoded word
        return output_array

