from collections import deque

class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
            rows, cols = len(heights), len(heights[0])
            p_que = deque()
            p_set = set()
            a_que = deque()
            a_set = set()

            for r in range(rows):
                p_que.append((r,0))
                p_set.add((r,0))
                a_que.append((r, cols - 1))
                a_set.add((r, cols - 1))
            
            for c in range(cols):
                p_que.append((0,c))
                p_set.add((0,c))
                a_que.append((rows - 1, c))
                a_set.add((rows - 1, c))
            

            def get_coords(que, seen):
                while que:
                    for i in range(len(que)):
                        r , c = que.popleft()
                        for nr, nc in [(r + 1, c), (r -1 , c), (r, c + 1), (r, c - 1)]:
                            if 0 <= nr < rows and 0 <= nc < cols and (nr,nc) not in seen and heights[nr][nc] >= heights[r][c]:
                                seen.add((nr,nc))
                                que.append([nr,nc])
            
            get_coords(p_que, p_set)
            get_coords(a_que, a_set)

            return list(p_set.intersection(a_set))




