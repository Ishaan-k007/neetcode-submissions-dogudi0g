class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:


        ROWS, COLS = len(grid), len(grid[0])
        islands = 0
        visit = set()
        def bfs(r,c):
            
      
            queue = deque([(r, c)])
            visit.add((r, c))
            
            while queue:
                for i in range(len(queue)):
                    r, c = queue.popleft()

                    for dr, dc in [[0,1], [0,-1], [1,0], [-1,0]]:
                        nr, nc = r+dr, c+dc
                        if (min(nr, nc) < 0 or
                            nr == ROWS or nc == COLS or
                            (nr, nc) in visit or grid[nr][nc] == "0"):
                            continue
                        queue.append((nr, nc))
                        visit.add((nr, nc))

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == "1" and (r, c) not in visit:
                    bfs(r,c)
                    islands += 1

        return islands
