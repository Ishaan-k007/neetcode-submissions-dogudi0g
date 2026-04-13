class Solution:
    def validWordSquare(self, words: List[str]) -> bool:
        column_array = []

        for i in range(len(words)):
            column_word = ""
            for word in words:
                if i < len(word):
                    column_word += word[i]
            column_array.append(column_word)

        return words == column_array


            
                
        