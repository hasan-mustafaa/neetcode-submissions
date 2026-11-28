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

        """
        Note, on the last loop, if everything is ROTTEN, we still have to process
        the new layer of ROTTEN, even if there's nothing left to infect
        This causes the minutes to be 1 higher than the expected

        Soloution: 
        - Each loop check if num_fresh is still greater than 0
        - This allows us to break early, before we reach minutes passed
        - Can either be while loop conditions or if condition in per node work
        """
        while que and num_fresh > 0:
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
        
        return min_passed if num_fresh == 0 else - 1


