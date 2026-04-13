class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        
        # sort the positions into a new descending sorted array 
        # put in stack anything lower than the bottom value in terms of time will form a flee
        # compute time for each position append them to stack
        dictionary = {} 
        sorted_positions = sorted(position, reverse = True)
        stack = []
        for i in range(len(position)):
            dictionary[position[i]] = speed[i]
        for i in range(len(position)):
            time = (target - sorted_positions[i]) / dictionary[sorted_positions[i]]
            if not stack or time > stack[-1]:
                stack.append(time)  
        return len(stack)