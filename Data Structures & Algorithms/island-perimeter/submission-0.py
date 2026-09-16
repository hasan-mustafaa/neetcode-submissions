class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        visited = set()
        rows, cols = len(grid), len(grid[0])

        def dfs(r, c):
            nonlocal rows, cols, visited

            if r >= rows or c >= cols or r < 0 or c < 0 or grid[r][c] == 0:
                return 1
            
            if (r,c) in visited:
                return 0
            
            visited.add((r,c))
            perimeter = dfs(r, c + 1)
            perimeter += dfs(r, c - 1)
            perimeter += dfs(r + 1, c)
            perimeter += dfs(r - 1, c)

            return perimeter


        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if grid[row][col] == 1:
                    return dfs(row, col)



            


