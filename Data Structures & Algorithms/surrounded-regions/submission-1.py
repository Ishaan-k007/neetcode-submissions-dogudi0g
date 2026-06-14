class Solution:
    def solve(self, board: List[List[str]]) -> None:
        # Any O connected to a border O cannot be surrounded, so mark those first. Then flip every remaining O to X.

        # dfs approach start at every 0 in the border and go as deep as possible add them to a set then for every co ordinate in the set flip from 0 to X 

        
        ROWS, COLS = len(board), len(board[0])
        visit = set()


        def dfs(r,c,visit):
            if ((r,c) in visit or r < 0 or c < 0 or r == ROWS or c == COLS or board[r][c] == "X"):

                return
            
            visit.add((r,c))
            dfs(r + 1, c, visit)
            dfs(r - 1, c, visit)
            dfs(r, c + 1, visit)
            dfs(r, c - 1, visit)

        for c in range(COLS):
            if board[0][c] == "O":
                dfs(0,c,visit)
            if board[ROWS - 1][c] == "O":
                dfs(ROWS - 1,c,visit)
        for r in range(ROWS):
            if board[r][0] == "O":
                dfs(r,0,visit)
            if board[r][COLS - 1] == "O":
                dfs(r,COLS - 1,visit)
        
        for r in range(ROWS):
            for c in range(COLS):
                if board[r][c] == "O" and (r,c) not in visit:
                    board[r][c] = "X"
        
