class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        


        # BFS algorithm starting from all the treasure chests
        # start from the co ordinates of treasure for each level replace the other co ordinates with the level

        ROWS , COLS = len(grid) , len(grid[0])

        queue = deque()
        visit = set()

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 0:
                    queue.append((r,c))
                    visit.add((r,c))
        
        level = 1
        while queue:
            for _ in range(len(queue)):
                r,c = queue.popleft()

                directions = [[0,1],[1,0],[0,-1],[-1,0]]

                for dr , dc in directions:
                    nr , nc = r + dr , c + dc

                    if min(nr,nc) < 0 or nr == ROWS or nc == COLS or ((nr,nc)) in visit or grid[nr][nc] == -1:
                        continue
                    
                    grid[nr][nc] = level
                    queue.append((nr,nc))
                    visit.add((nr,nc))
            level += 1
