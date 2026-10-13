class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        EMPTY, FRESH, ROTTEN = 0, 1, 2
        rows, cols = len(grid), len(grid[0])
        queue = deque()

        #Counters
        fresh_fruit = 0

        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == ROTTEN:
                    queue.append([row,col])
                elif grid[row][col] == FRESH:
                    fresh_fruit += 1
        
        if fresh_fruit == 0:
            return 0
        
        #steps replacement
        minutes = 0
        while queue and fresh_fruit > 0:
            for i in range(len(queue)):
                r, c = queue.popleft()

                for nr, nc in [(r + 1, c), (r - 1,c), (r, c + 1), (r, c - 1)]:
                    if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] == FRESH:
                        grid[nr][nc] = ROTTEN
                        queue.append([nr,nc])
                        fresh_fruit -= 1


            minutes += 1
            
        

        return minutes if not fresh_fruit  else -1




"""
- Fill Queue
- While queue
- if fresh = 0 return
"""