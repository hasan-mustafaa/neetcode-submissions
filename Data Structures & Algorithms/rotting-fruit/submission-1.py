class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        EMPTY, FRESH, ROTTEN = 0, 1, 2
        rows, cols = len(grid), len(grid[0])
        num_fresh = 0
        q = deque()
       

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == ROTTEN:
                    q.append([r,c])
                elif grid[r][c] == FRESH:
                    num_fresh += 1
        
        if num_fresh == 0:
            return 0
        

        num_min = -1
        while q:
            num_min += 1
            for i in range(len(q)):
                r, c = q.popleft()
                for r, c in [(r + 1, c), (r - 1, c), (r, c + 1), (r, c - 1)]:
                    if 0 <= r < rows and 0 <= c < cols and grid[r][c] == FRESH:
                        grid[r][c] = ROTTEN
                        num_fresh -= 1
                        q.append([r,c])
            
        
        if num_fresh == 0:
            return num_min
        else:
            return -1

        

