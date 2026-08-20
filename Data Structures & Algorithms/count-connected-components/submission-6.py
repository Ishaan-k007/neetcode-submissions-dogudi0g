class DSU:
    def __init__(self, n):
        self.parent = list(range(n))
        self.rank = [1] * n

    # find the root parent 
    def find(self, node):
        cur = node

        while cur != self.parent[cur]:
            self.parent[cur] = self.parent[self.parent[cur]]
            cur = self.parent[cur]
        return cur

    def union(self, u, v):
        pu = self.find(u)
        pv = self.find(v)

        if pu == pv:
            return False
        
        if self.rank[pv] > self.rank[pu]:
            self.parent[pu] = pv
            self.rank[pv] += self.rank[pu]
        else:
            self.parent[pv] = pu
            self.rank[pu] += self.rank[pv]
        return True
    
    






class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        dsu = DSU(n)
        res = n
        for n1,n2 in edges:
            if dsu.union(n1,n2):
                res -=  1
        return res