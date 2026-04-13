import math
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:

        ## brute force:
        # for each point in the list compute distance then return the k points that have the least distance
        # create dictionary and append the distance for each point
        distance  = {}
        for x, y in points:
            distance[(x, y)] = (x**2 + y**2) ** 0.5
        
        sorted_dict = dict(sorted(distance.items(), key=lambda item: item[1]))

        res = []
        count = 1
        for key in sorted_dict:
            if count > k:
                break
            res.append(key)
            count += 1
        return res

        


        