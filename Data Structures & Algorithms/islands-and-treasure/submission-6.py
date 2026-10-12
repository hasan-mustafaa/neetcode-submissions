class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        rows, cols = len(grid), len(grid[0])
        queue = deque()
        visited = set()

        def add_cell(row, col):
            if row < 0 or row >= rows or col < 0 or col >= cols or (row,col) in visited or grid[row][col] == -1:
                return
            queue.append([row,col])
            visited.add((row,col))

        
        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == 0:
                    queue.append([row,col])
                    visited.add((row, col))
                
        dist = 0
        while queue:
            for i in range(len(queue)):
                r,c = queue.popleft()
                grid[r][c] = dist

                add_cell(r + 1, c)
                add_cell(r - 1, c)
                add_cell(r, c + 1)
                add_cell(r, c - 1)
            dist += 1

                


        




