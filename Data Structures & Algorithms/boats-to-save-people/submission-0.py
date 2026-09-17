class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        # sorting the array
        # using a 2 pointer approach - if can do R and L otherwise just R then -1 from R and add one from L
        

        # [5,1,4,2]
        # [1,2,4,5]
        # 2,4  
        # [1,3,2,3,2]
        # [1,2,2,3,3]
        # L        R
        # L      R
        # L    R
        #   LR   
        people.sort()
        L = 0
        R = len(people) - 1

        boats = 0
        while L < R:
            if people[R] + people[L] <= limit:
                R -= 1
                L += 1
            else:
                R -= 1
            


            boats += 1
        if L == R:
            boats += 1
        return boats

        