class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:

        indegree = [0] * numCourses     # how many dependencies each node has 

        adj = [[] for _ in range(numCourses)]     # maps dependencies -> dependant

        for src , dst in prerequisites:
            indegree[dst] += 1
            adj[src].append(dst)

        
        q = deque()

        # add all nodes that have no dependencies to the graph
        for n in range(numCourses):
            if indegree[n] == 0:
                q.append(n)

        finish = 0
        while q:
            node = q.popleft()
            finish += 1

            for nei in adj[node]:
                indegree[nei] -= 1
                if indegree[nei] == 0:
                    q.append(nei)


        return finish == numCourses 
        




        
        