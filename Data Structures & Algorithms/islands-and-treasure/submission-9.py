
from collections import deque
class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        LAND = 2147483647
        rows, cols = len(grid), len(grid[0])
        visited = set()
        que = deque()


        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 0:
                    que.append((r, c))
                    visited.add((r, c))
        
        distance = 0
        while que:
            for i in range(len(que)):
                r, c = que.popleft()
                grid[r][c] = distance
            
                for nr, nc in ((r + 1, c), (r - 1, c), (r, c + 1), (r, c - 1)):
                    if (0 <= nr < rows  
                    and 0 <= nc < cols 
                    and (nr, nc) not in visited
                    and grid[nr][nc] == LAND):

                        que.append((nr, nc))
                        visited.add((nr, nc))

            distance += 1
        

                

        