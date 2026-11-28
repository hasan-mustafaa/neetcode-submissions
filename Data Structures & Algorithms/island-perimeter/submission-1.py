class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        visited = set()
        perimeter = 0

        for r in range(rows):
            for c in range(cols):

                if grid[r][c] == 1:

                    for nr, nc in ((r + 1, c), (r - 1, c), (r, c + 1), (r, c - 1)):
                        
                        if (nr, nc) in visited:
                            continue
                        
                        if (nr < 0 or nr >= rows 
                        or nc < 0 or nc >= cols
                        or grid[nr][nc] == 0 ):
                            perimeter += 1

                        
                    visited.add((r, c))

        return perimeter
