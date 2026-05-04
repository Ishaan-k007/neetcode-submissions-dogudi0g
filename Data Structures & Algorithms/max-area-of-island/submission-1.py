class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:

        # BFS implementation

        ROWS, COLS = len(grid), len(grid[0])
        visit = set()
        max_sum = 0
        


        def bfs(r,c,grid,ROWS,COLS):
            
            queue = deque()
            queue.append((r,c))
            visit.add((r,c))

            length = 1
            while queue:
                for i in range(len(queue)):
                    r, c = queue.popleft()

                    for dr, dc in [[0,1], [0,-1], [1,0], [-1,0]]:
                        nr, nc = r+dr, c+dc
                        if (min(nr, nc) < 0 or
                            nr == ROWS or nc == COLS or
                            (nr, nc) in visit or grid[nr][nc] == 0):
                            continue
                        queue.append((nr, nc))
                        visit.add((nr, nc))
                        print("adding")
                        length += 1
            return length


        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 1:
                    if (r,c) not in visit:
                        print("Hi")
                        current_sum = bfs(r,c,grid,ROWS,COLS)
                        max_sum = max(current_sum,max_sum)
        
        return max_sum



                