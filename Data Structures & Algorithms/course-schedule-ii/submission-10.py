class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        


        indegree = [0] * numCourses

        adj_list = [[] for _ in range(numCourses)]

        for dst, src in prerequisites:
            indegree[dst] += 1
            adj_list[src].append(dst)


        q = deque()
        res = []
        for i in range(numCourses):
            if indegree[i] == 0:
                res.append(i)
                q.append(i)

        while q:
            node = q.popleft()

            for nei in adj_list[node]:
                indegree[nei] -= 1
                if indegree[nei] == 0:
                    res.append(nei)
                    q.append(nei)
        
        if len(res) == numCourses:
            return res
        else:
            return []
            
        
            
        