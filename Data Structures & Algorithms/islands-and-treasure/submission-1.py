class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        
        
        
        ROWS, COLS = len(grid), len(grid[0])
     
        

        def bfs(r,c,grid):
            
            visit = set()
            queue = deque()
            queue.append((r, c))
            visit.add((r, c))

            length = 0
            while queue:
                for i in range(len(queue)):
                    r, c = queue.popleft()
                    if grid[r][c] > 0:
                        min_val = min(grid[r][c], length)
                        grid[r][c] = min_val

                    for dr, dc in [[0,1], [0,-1], [1,0], [-1,0]]:
                        nr, nc = r+dr, c+dc
                        if (min(nr, nc) < 0 or
                            nr == ROWS or nc == COLS or
                            (nr, nc) in visit or grid[nr][nc] == -1):
                            continue
                        queue.append((nr, nc))
                        visit.add((nr, nc))
                length += 1
            
            return grid
            
         

        
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 0:
                    print("HI")
                    grid = bfs(r,c,grid)
        
        print(grid)
   


