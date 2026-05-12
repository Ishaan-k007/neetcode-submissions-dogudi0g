class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:

        # map each course to its pre reqs
        # store all courses along the current DFS path - (for cycle detection)
        # do dfs and see if the list returns a node with no pre req

        from collections import defaultdict
        preMap = defaultdict(list)


        for crs,pre in prerequisites:
            # append and not = as you are adding to list not replacing the value of the key
            preMap[crs].append(pre)

        
        visit = set()

        def dfs(crs):

            # cycle detected

            if crs in visit:
                return False

            # no more pre reqs for the course ;
            if preMap[crs] == []:
                return True

            visit.add(crs)

            # for course to be accepted every pre requiste must be able to be done (no cycle in any of the pre reqs)
            for pre in preMap[crs]:
                if not dfs(pre):
                    return False

            # if no false has been returned we no for none of the pre reqs there is a cycle so you can do this course 
            # backtrack
            visit.remove(crs)
            # since we have confirmed that we can do everything for this crs we can just say that the course has no pre req
            preMap[crs] = []
            return True

            # for any course if it returns false you cant do all the courses

        for c in range(numCourses):
            if not dfs(c):
                return False
        return True