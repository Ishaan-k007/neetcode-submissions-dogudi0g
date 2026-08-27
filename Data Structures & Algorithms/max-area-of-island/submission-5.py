class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:

        # BFS sol start at every 1 and increment the count for the size of the island

        ROWS, COLS = len(grid), len(grid[0])
        visit = set()

        def bfs(r,c,visit):
            
            area = 1
            queue = deque([(r,c)])
            visit.add((r,c))
            while queue:
                r,c = queue.popleft()

                directions = [[0,1],[0,-1],[1,0],[-1,0]]

                for dr , dc in directions:
                    nr , nc = r + dr, c+ dc

                    if min(nr,nc) < 0 or nr == ROWS or nc == COLS or (nr,nc) in visit or grid[nr][nc] == 0:
                        continue
                    area += 1
                    
                    queue.append((nr,nc))
                    visit.add((nr,nc))

            return area

        max_area = 0
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 1 and (r,c) not in visit:
                    cur_area = bfs(r,c,visit)
                    max_area = max(max_area, cur_area)
        return max_area

                    