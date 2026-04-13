class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        # create additional stack storing indicies 
        # if stack value > top of the stack pop of the top of the stack and return indicies in res 
        # keep popping till less 
        # for all the remaining items in the stack return 0 

        stack = []
        n = len(temperatures)
        res = [0] * n
        for i in range(len(temperatures)):
            
             
            if stack:

                while stack and temperatures[i] > temperatures[stack[-1]]:
                    index = stack.pop()
                    print(i-index)
                    res[index] = i - index
                

            
            stack.append(i)
            print(stack)

        if stack:
            for _ in range(len(stack)):
                idx = stack.pop()
                res[idx] = 0
        return res
        


        