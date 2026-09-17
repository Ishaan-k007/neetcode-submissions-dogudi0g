class UnionFind:

    def __init__(self,n):
        self.parent = list(range(n))
        self.rank = [1] * n

    def find(self, node):

        while node != self.parent[node]:
            node = self.parent[node]
        return node
    
    def union(self, node1,node2):

        parent1 = self.find(node1)
        parent2 = self.find(node2)

        if parent1 == parent2:
            return False

        if self.rank[parent1] < self.rank[parent2]:
            self.parent[parent1] = parent2
            self.rank[parent2] += self.rank[parent1]
        else:
            self.parent[parent2] = self.parent[parent1]
            self.rank[parent1] += self.rank[parent2]
        return True

    





class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        dsu = UnionFind(n)
        count = n
        for u,v in edges:
            if dsu.union(u,v):
                count -= 1
        return count
