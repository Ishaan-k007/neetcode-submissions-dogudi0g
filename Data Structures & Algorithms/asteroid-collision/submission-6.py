class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:

        # if asteroid is positive direction add to a stack
        # if negative direction check if it can pop off the stack
        # repeat untill negative asteroid is destroyed or start of stack is reached

        # [2,4,-5,3]   -> [-5,3]


        stack = []
        
        for i in range(len(asteroids)):
            alive = True
            if asteroids[i] >= 0:
                stack.append(asteroids[i])

            else:
                    
                while stack and stack[-1] > 0 and stack[-1] <= abs(asteroids[i]):
                    if stack[-1] == abs(asteroids[i]):
                        stack.pop()
                        alive = False
                        break
                    else:
                        stack.pop()
                
                if stack and stack[-1] > abs(asteroids[i]):
                    alive = False

                if alive:
                    stack.append(asteroids[i])
        return stack
