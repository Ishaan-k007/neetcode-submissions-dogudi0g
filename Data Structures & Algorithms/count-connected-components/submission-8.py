class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:


        adj_list = [[] for _ in range(n)]

        for u,v in edges:
            adj_list[u].append(v)
            adj_list[v].append(u)

        visit = set()
        def bfs(start):
            
            queue = deque()
            queue.append(start)
  
            while queue:
                node = queue.popleft()

                for nei in adj_list[node]:
                    if nei not in visit:
                        queue.append(nei)
                        visit.add(nei)

        count = 0
        for i in range(n):
            if i not in visit:
                bfs(i)
                visit.add(i)
                count += 1
        return count
            


        