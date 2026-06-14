from collections import deque 
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
    
        # edge case: do I have rotten fruit?

        # queue initially with all the rotten fruit
        # BFS on the grid i start at the rotten fruits and every iteration of the BFS i turn fresh fruit rotten
        # and then i add all non empty into the queue 
        # untill theres nothing in the queue
        # i keep a reference for how many fresh fruit there is and at the end if it is 0 i return the num of iterations otherwise ill return -1


        ROWS, COLS = len(grid) , len(grid[0])

        fresh = 0
        queue = deque()
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 2:
                    queue.append((r,c))
                if grid[r][c] == 1:
                    fresh += 1
        
        visit = set()
        def bfs():
            nonlocal fresh

            minutes = 0

            while queue and fresh:

                for i in range(len(queue)):
                    r,c = queue.popleft()

                    directions = [[0,1],[0,-1],[1,0],[-1,0]]

                    for dr, dc in directions:
                        nr, nc = r + dr, c + dc

                        if (min(nr,nc) < 0) or nr == ROWS or nc == COLS or (nr,nc) in visit or grid[nr][nc] == 0 or grid[nr][nc] == 2:

                            continue
                        
                        queue.append((nr,nc))
                        visit.add((nr,nc))
                        fresh -= 1
                minutes += 1
            return minutes
        
        minutes = bfs()
        if fresh == 0:
            return minutes
        else:
            return -1 






