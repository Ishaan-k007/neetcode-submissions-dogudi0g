class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        

        # have 2 hashsets one for pacific and one for atlantic
        # dfs from all the pacific ones and add to pacific set
        # same for atlantic
        # id 
        ROWS , COLS = len(heights), len(heights[0])
        def dfs(r,c,visit,prev_height):

            if min(r,c) < 0 or (r,c) in visit or r == ROWS or c == COLS or heights[r][c] < prev_height:
                return
            visit.add((r,c))
           
                
            dfs(r + 1,c,visit,heights[r][c])
            dfs(r - 1,c,visit,heights[r][c])
            dfs(r,c + 1,visit,heights[r][c])
            dfs(r,c - 1,visit,heights[r][c])
        

        # for all pacific ones
        pacific = set()
        atlantic = set()
        for i in range(ROWS):
            for j in range(COLS):

                if j == 0:
                    dfs(i,j,pacific,heights[i][j])
                if i == 0:
                    dfs(i,j,pacific,heights[i][j])
                if j == COLS - 1:
                    dfs(i,j,atlantic,heights[i][j])
                if i == ROWS - 1:
                    dfs(i,j,atlantic,heights[i][j])

        return list(pacific & atlantic)


            

            

        