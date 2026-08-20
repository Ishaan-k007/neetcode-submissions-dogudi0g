class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        
        num_of_pre_reqs_left = [0] * numCourses

        adj = [[] for i in range(numCourses)]

        for after,pre  in prerequisites:
            num_of_pre_reqs_left[after] += 1
            adj[pre].append(after)


        queue = deque()

        for i in range(numCourses):
            if num_of_pre_reqs_left[i] == 0:
                queue.append(i)

        finish = 0
        while queue:
            node = queue.popleft()
            finish += 1

            for nei in adj[node]:
                num_of_pre_reqs_left[nei] -= 1
                if num_of_pre_reqs_left[nei] == 0:
                    queue.append(nei)
        return finish == numCourses