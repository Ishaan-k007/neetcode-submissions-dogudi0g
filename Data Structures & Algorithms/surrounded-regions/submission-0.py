class Solution:
    def solve(self, board: List[List[str]]) -> None:
        # Any O connected to a border O cannot be surrounded, so mark those first. Then flip every remaining O to X.

        # dfs approach start at every 0 in the border and go as deep as possible add them to a set then for every co ordinate in the set flip from 0 to X 

        ROWS, COLS = len(board), len(board[0])
        visit = set()

        
        
        def dfs(board, r, c, visit):

  
           
            if (min(r,c) < 0 or r == ROWS or c == COLS or (r, c) in visit or board[r][c] == "X"):
                return 
        

            
          
                
            visit.add((r, c))
              
         
            dfs(board, r + 1, c, visit)   # down
            dfs(board, r - 1, c, visit)   # up
            dfs(board, r, c + 1, visit)   # right
            dfs(board, r, c - 1, visit)   # left
            return
        

        for i in range (ROWS):
            # on first and last column
            # need to check first if it is 0
            if board[i][0] == "O": 
                dfs(board,i,0,visit)
            if board[i][COLS-1] == "O":
                dfs(board,i,COLS-1,visit)

            
        
        for i in range(COLS):

            if board[0][i] == "O":
                dfs(board,0,i,visit)
            if board[ROWS-1][i] == "O":
                dfs(board,ROWS-1,i,visit)

    
        for x in range(ROWS):
            for y in range(COLS):
                if board[x][y] == "O" and (x,y) not in visit:
                    board[x][y] = "X"
                    
        
        