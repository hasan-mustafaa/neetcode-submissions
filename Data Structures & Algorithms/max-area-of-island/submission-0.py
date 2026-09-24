class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        max_area = 0
        curr_area = 0

        def dfs(r,c):
            nonlocal curr_area, max_area

            if r < 0 or r >= rows or c < 0 or c >= cols or grid[r][c] != 1:
                return
            else:
                grid[r][c] = 0
                curr_area += 1
                max_area = max(curr_area, max_area)
                dfs(r + 1, c)
                dfs(r - 1, c)
                dfs(r, c + 1)
                dfs(r, c - 1)
        

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    dfs(r,c)
                    curr_area = 0
        
        return max_area