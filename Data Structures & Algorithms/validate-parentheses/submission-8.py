class Solution:
    def isValid(self, s: str) -> bool:
        
        bracket_set = {"(" : ")","{" : "}", "[" : "]"}
        stack = []

        for i in range(len(s)):

            if s[i] in bracket_set:
                stack.append(s[i])
            elif stack and bracket_set[stack[-1]] == s[i]:
                stack.pop()
            else:
                return False
        
        if stack:
            return False
        else:
            return True

        
        
        