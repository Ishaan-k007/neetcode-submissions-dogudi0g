class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:

        indegree = [0] * numCourses

        adj_list = [[] for _ in range(numCourses)]

        for u,v in prerequisites:
            adj_list[v].append(u)
            indegree[u] += 1
        

        queue = deque()
        for i in range(numCourses):
            if indegree[i] == 0:
                queue.append(i)
        
        finish = 0
        while queue:
            node = queue.popleft()
            finish += 1
            for nei in adj_list[node]:
                indegree[nei] -= 1
                if indegree[nei] == 0:
                    queue.append(nei)
        
        return finish == numCourses 

        