class Solution:

    def encode(self, strs: List[str]) -> str:
        
        result = ""
        for string in strs:
            result += string + "¬"
        print(result)
        return result

    def decode(self, s: str) -> List[str]:
        individual_string = s.split("¬")
        

        individual_string = individual_string[:len(individual_string)-1]
        print(individual_string)
        return individual_string
