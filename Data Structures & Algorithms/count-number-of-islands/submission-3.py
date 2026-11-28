class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        rows, cols = len(grid), len(grid[0])
        visited = set()
        num_islands = 0

        def dfs(r, c):

            if (r < 0 or r >= rows or c < 0 or c >= cols
                or (r, c) in visited 
                or grid[r][c] == "0"):
                return 
            
            visited.add((r,c))

            for nr, nc in ((r + 1, c), (r - 1, c), (r, c + 1), (r, c - 1)):
                dfs(nr, nc)
        

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == "1" and (r, c) not in visited:
                    num_islands += 1
                    dfs(r, c)
        
        return num_islands
        

            