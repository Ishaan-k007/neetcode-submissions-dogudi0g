class UnionFind:   
        def __init__(self, n):
    # rank of a node is simply its height (in this case 0 -> 1 0 would have a height of 1
            self.par = {}
            self.rank = {}
    # At the start for every node n its parent is itself and its rank is 0
            for i in range(n):
                self.par[i] = i
                self.rank[i] = 0
        
        # Find parent of n, with path compression.
        def find(self, n):
        # start at the nodes parent 
            p = self.par[n]
        # keep climning while p is not a root - this is determined by p's parent pointing to itself
            while p != self.par[p]:
            # path compression line if 1 -> 2 -> 3 3s parent is set from 2 to 1 
                self.par[p] = self.par[self.par[p]]
                # move up to new root 
                p = self.par[p]
            return p

        # Union by height / rank.
        # Return false if already connected, true otherwise.
        def union(self, n1, n2):
            # find the root of 2 nodes If two nodes share the same root, they're already in the same group.
            p1, p2 = self.find(n1), self.find(n2)
            if p1 == p2:
                # already in same group
                return False
            
            # union by rank always attach the shorter tree under the taller one to keep 
            # the overall tree shallow. 
            if self.rank[p1] > self.rank[p2]:
                self.par[p2] = p1
            elif self.rank[p1] < self.rank[p2]:
                self.par[p1] = p2
            # else arbitary parent 
            else:
                self.par[p1] = p2
                self.rank[p2] += 1
            return True

class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        uf = UnionFind(n)
        count = n
        for u, v in edges:
            if uf.union(u, v):
                count -= 1
        return count

    
       