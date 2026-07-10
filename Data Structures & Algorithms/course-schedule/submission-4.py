class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # need to store all pre reqs for a certain subject

        pre_req = defaultdict(list)

        for requisite in prerequisites:
            pre_req[requisite[0]].append(requisite[1])
        

        memo = {}
        visited = set()

        def dfs(node,visited):

            if node in visited:
                return False
            if node in memo:
                return memo[node]
            visited.add(node)
            neighbours = pre_req[node]

            for neighbour in neighbours:

                boolean = dfs(neighbour,visited)
                if boolean is not True:
                    return False
            visited.remove(node)
            memo[node] = True
            return True
        
        
        for prerequisite in prerequisites:
            if prerequisite[0] not in visited:
               boolean = dfs(prerequisite[0],visited)
               if boolean is not True:
                return False
        return True

            


        
                


