from collections import deque
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        EMPTY, FRESH, ROTTEN = 0, 1, 2
        rows, cols = len(grid), len(grid[0])
        que = deque()
        num_fresh = 0

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == ROTTEN:
                    que.append((r,c))
                if grid[r][c] == FRESH:
                    num_fresh += 1
        
        min_passed = 0
        if num_fresh == 0:
            return min_passed
        
        while que:
            for i in range(len(que)):
                r, c = que.popleft()
            
                for nr, nc in ((r + 1, c), (r - 1, c), (r, c + 1), (r, c - 1)):
                    if (0 <= nr < rows
                        and 0 <= nc < cols
                        and grid[nr][nc] == FRESH):
                        que.append((nr, nc))

                        #Rotten in Queue, makes surrounding Fresh Rotten
                        #It affects neighbour nodes, not the node in the queue
                        #This is why this is per neighbour not per node
                        grid[nr][nc] = ROTTEN
                        num_fresh -= 1
            
            min_passed += 1
        
        return min_passed - 1if num_fresh == 0 else - 1


