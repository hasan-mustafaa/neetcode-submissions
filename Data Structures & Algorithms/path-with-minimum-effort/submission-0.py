import heapq
class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        rows, cols = len(heights), len(heights[0])
        visited = set()
        minHeap = [(0, 0, 0)]

        while minHeap:
            dist, r, c = heapq.heappop(minHeap)

            if (r, c) in visited:
                continue
            
            visited.add((r,c))

            if r == rows - 1 and c == cols - 1:
                return dist
            

            for r2, c2 in ((r + 1, c), (r - 1, c), (r, c + 1), (r, c - 1)):
                if 0 <= r2 < rows and 0 <= c2 < cols and (r2, c2) not in visited:
                    step = abs(heights[r2][c2] - heights[r][c])
                    new_dist = max(dist, step)
                    heapq.heappush(minHeap, (new_dist, r2, c2))
               
        return -1