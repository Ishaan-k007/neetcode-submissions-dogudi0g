class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:


        # gonna use a BFS approach to seperate grid into islands
        # for each island count how many cells it has max cells wins

        # Time + Space Complexity = O(m*n)

        ROWS, COLS = len(grid), len(grid[0])
       
        visit = set()
        res_count = 0
        
        def bfs(r,c):
            count = 0
            queue = deque([(r, c)])
            visit.add((r, c))
            
            while queue:
                for i in range(len(queue)):
                    count += 1
                    r, c = queue.popleft()

                    for dr, dc in [[0,1], [0,-1], [1,0], [-1,0]]:
                        nr, nc = r+dr, c+dc
                        if (min(nr, nc) < 0 or
                            nr == ROWS or nc == COLS or
                            (nr, nc) in visit or grid[nr][nc] == 0):
                            continue
                        queue.append((nr, nc))
                        visit.add((nr, nc))
            return count

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 1 and (r, c) not in visit:
                    cur_count = bfs(r,c)
                    res_count = max(cur_count,res_count)

        return res_count
