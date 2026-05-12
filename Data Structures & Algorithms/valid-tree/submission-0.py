class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:




        # Map each course to its edges - BIDERICTIONAL VERSION
        graph = {i: [] for i in range(n)}

        for a, b in edges:  
            graph[a].append(b)
            graph[b].append(a)

        print(graph)

        # Store all courses along the current DFS path
        visiting = set()
        num_visited = set()

        def dfs(crs,parent):
            if crs in visiting:
                return False

            num_visited.add(crs)
            visiting.add(crs)
            for pre in graph[crs]:
                if pre == parent:
                    continue
                if not dfs(pre,crs):
                    return False
            visiting.remove(crs)


            return True

        if not dfs(0,-1):
            return False
        if len(num_visited) != n:
            return False
        return True