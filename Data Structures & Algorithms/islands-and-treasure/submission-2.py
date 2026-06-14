from collections import deque
class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        
        # start at every treasure and do bfs taking a note of distance (level)
        # if it hits land replace value with min of land cuurent and level


        
        visit = set()
        ROWS, COLS = len(grid), len(grid[0])
        treasures = deque()
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 0:
                    treasures.append((r,c))
        
        
 

        def bfs():
            
            
            level = 1
            while treasures:
                for i in range(len(treasures)):
                    r,c = treasures.popleft()
                    directions = [[0,1],[0,-1],[1,0],[-1,0]]
                    for dr,dc in directions:
                        nr,nc = r +dr , c+dc

                        if (min(nr,nc) < 0) or nr == ROWS or nc == COLS or grid[nr][nc] == -1 or grid[nr][nc] == 0 or (nr,nc) in visit :
                            continue
                        # what happends when meets land
                        if grid[nr][nc] == 2147483647:
                            grid[nr][nc] = level
                        treasures.append((nr,nc))
                        visit.add((nr,nc))
                level += 1

        bfs()



        
        
        