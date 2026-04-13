class Solution:
    def generateParenthesis(self, n: int) -> List[str]:


        
        res = []
        def backtrack(substring,n):
            nonlocal res

            if len(substring) == n*2:
                if check_substring(substring):
                     res.append("".join(substring))
                return
                

            
            substring.append("(")
            backtrack(substring,n)
            substring.pop()
            substring.append(")")
            backtrack(substring,n)
            substring.pop()
        

        def check_substring(substring):
            stack = []

            for i in range(len(substring)):
                if substring[i] == "(":
                    stack.append("(")
                if substring[i] == ")":

                    if stack and stack[-1] == "(":
                        stack.pop()
                    else:
                        return False
            if len(stack) == 0:
                return True
            return False
        backtrack([],n)
        return res
                
