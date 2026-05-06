class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
    
        ROWS, COLS = len(grid), len(grid[0])
        q = deque()
        fresh = 0

        # Add all rotten oranges first into a queue thats passed into bfs
        # Also count how many fresh fruit there is  
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 2:
                    q.append((r, c))
                elif grid[r][c] == 1:
                    fresh += 1

        def bfs():

            # while there is still rotting fruit and there is still fresh fruit run bfs 
            # if the fruit is not fresh ignore 
            # if it is fresh turn to rotten and add it to the queue -> this now enables the fruits adjacent to it to get infected
            # if there is still fresh fruit then return -1 else return minutes the levels
            nonlocal fresh

            minutes = 0
            directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]

            while q and fresh > 0:
                for _ in range(len(q)):
                    r, c = q.popleft()

                    for dr, dc in directions:
                        nr, nc = r + dr, c + dc

                        if (
                            nr < 0 or nc < 0 or
                            nr >= ROWS or nc >= COLS or
                            grid[nr][nc] != 1
                        ):
                            continue

                        grid[nr][nc] = 2
                        fresh -= 1
                        q.append((nr, nc))

                minutes += 1

            return minutes

        answer = bfs()

        return answer if fresh == 0 else -1