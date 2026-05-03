class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:

        def dfs(grid, r, c, visit):
            ROWS, COLS = len(grid), len(grid[0])
            if (min(r, c) < 0 or r == ROWS or c == COLS  or grid[r][c] == 0):
                return 1

            if (r, c) in visit:
                return 0
            

            visit.add((r,c))
            count = 0
            count += dfs(grid, r + 1, c, visit)   # down
            count += dfs(grid, r - 1, c, visit)   # up
            count += dfs(grid, r, c + 1, visit)   # right
            count += dfs(grid, r, c - 1, visit)   # left
            
            return count
        
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == 1:
                    return dfs(grid, r, c, set())
            
        



        

