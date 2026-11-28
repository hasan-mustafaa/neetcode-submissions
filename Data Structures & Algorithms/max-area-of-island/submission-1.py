class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        visited = set()
        max_area = 0
        curr_area = 0

        def dfs(r, c):
            nonlocal curr_area

            if (r < 0 or r >= rows
                or c < 0 or c >= cols
                or (r, c) in visited
                or grid[r][c] == 0):
                return
            
            visited.add((r,c))
            curr_area += 1

            for nr, nc in ((r + 1, c), (r - 1, c), (r, c + 1), (r, c - 1)):
                dfs(nr, nc)
        

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1 and (r,c) not in visited:
                    dfs(r, c)
                    max_area = max(curr_area, max_area)
                    curr_area = 0
        
        return max_area 