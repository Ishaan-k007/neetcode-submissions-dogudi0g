class MyQueue:

    def __init__(self):
        self.stack1 = []
        self.stack2 = []
        
        

    def push(self, x: int) -> None:
        self.stack1.append(x)

        

    def pop(self) -> int:
        # if the second stack is null 
        # pop each element from the first stack and add it to second stack 
        # now this is the reversed stack (queue implementation so can pop)
        # we can keep popping until empty
        # if we want to keep pushing we can still push to stack 1
        # if stack 2 becomes empty again repeat the process and pop each element from the first stack and add it to second stack 
        # Amortized this is O(1)  


        if self.empty():
            return []
        if len(self.stack2) == 0:
            for _ in range(len(self.stack1)):
                self.stack2.append(self.stack1.pop())
        
        return self.stack2.pop()


        

    def peek(self) -> int:
        if self.empty():
            return []
        
        if len(self.stack2) == 0:
            for _ in range(len(self.stack1)):
                self.stack2.append(self.stack1.pop())
        
        return self.stack2[-1]

        

    def empty(self) -> bool:
        if len(self.stack1) == 0 and len(self.stack2) == 0:
            return True
        return False
        


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()