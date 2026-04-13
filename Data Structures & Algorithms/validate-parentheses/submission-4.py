class Solution:
    def isValid(self, s: str) -> bool:
        symbol_dict = {
                        "[" : "]",
                        "{" : "}",
                        "(" : ")"
        }
        symbol_stack = []
        for i in range(len(s)):
            if s[i] in symbol_dict:
                symbol_stack.append(s[i])
            else:
                if symbol_stack == []:
                    return False
                last_symbol = symbol_stack[-1]
                if s[i] == symbol_dict[last_symbol]:
                    symbol_stack.pop()
                else:
                    return False
        if symbol_stack == []:
            return True
        return False
        