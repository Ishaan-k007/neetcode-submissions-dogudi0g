class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        # Map each course to its prerequisites


        num_of_pre_reqs_needed = [0] * numCourses

        adj = [[] for i in range(numCourses)]

        for after,pre in prerequisites:
            num_of_pre_reqs_needed[after] += 1
            adj[pre].append(after)
        
        
         

        
        queue = deque()
        res = []
        finish = 0

        for i in range(numCourses):
            if num_of_pre_reqs_needed[i] == 0:
                queue.append(i)

        while queue:
            node = queue.popleft()
            res.append(node)
            finish += 1

            for nei in adj[node]:
                num_of_pre_reqs_needed[nei] -= 1

                if num_of_pre_reqs_needed[nei] == 0:
                    queue.append(nei)
        if finish == numCourses:
            return res
        else:
            return []
            
        
            
        