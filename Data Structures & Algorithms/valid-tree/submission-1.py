class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        #Recall the two fundamental mathematical properties of a tree: 1) It must be fully connected 
        #(all nodes reachable from each other), and 
        #2) It must contain exactly n - 1 edges to avoid cycles.
        if len(edges) > n - 1:
            return False

        adj = [[] for _ in range(n)]
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)

        visit = set()
        q = deque([(0, -1)])  # (current node, parent node)
        visit.add(0)
        #When you see a visited neighbour:

        #If it's your parent → ignore it (that's just the edge you came from).
        #If it's not your parent → you've found a cycle.
        while q:
            node, parent = q.popleft()
            for nei in adj[node]:
                if nei == parent:
                    continue
                if nei in visit:
                    return False
                visit.add(nei)
                q.append((nei, node))

        return len(visit) == n



        