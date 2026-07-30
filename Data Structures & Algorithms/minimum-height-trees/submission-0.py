class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:

        visit = set()
        for i in range(n):
            visit.add(i)

        graph = defaultdict(list)
        for edge in edges:
            word1 = edge[0]
            word2 = edge[1]
            graph[word1].append(word2)
            graph[word2].append(word1)


        print(graph)

        def dfs(node,visit,count):
            visit.add(node)
            if visit is None:
                return count
            
            max_count = count
            for nei in graph[node]:
                if nei not in visit:
                    max_count = max(max_count, dfs(nei, visit, count + 1))
            
            return max_count
        
        min_val = float("inf")
        res = []
        for i in range(n):
            cur_min = dfs(i,set(),0)
            if cur_min < min_val:
                min_val = cur_min
                res = []
                res.append(i)
            elif cur_min == min_val:
                res.append(i)
        return res 


        