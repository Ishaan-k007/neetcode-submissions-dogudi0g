class Solution:
    def evalRPN(self, tokens: List[str]) -> int:

        if len(tokens) == 1:
            return int(tokens[0])
        operators = ["+","-","*","/"]
        cur_stack = []
        cur_sum = 0
        for i in range(len(tokens)):
            if tokens[i] in operators:
                second_operator = int(cur_stack.pop())
                first_operator = int(cur_stack.pop())

                print(first_operator)
                print(second_operator)
                
                

                if tokens[i] == "+":
                    cur_sum = first_operator + second_operator
                elif tokens[i] == "-":
                    cur_sum = first_operator - second_operator
                elif tokens[i] == "*":
                    cur_sum = first_operator * second_operator
                else:
                    cur_sum = int(first_operator / second_operator)
                cur_stack.append(cur_sum)
                print("hi", cur_sum)
                print("hello", cur_stack)
        

            


            else:
                cur_stack.append(tokens[i])

        return cur_sum
            

            


        