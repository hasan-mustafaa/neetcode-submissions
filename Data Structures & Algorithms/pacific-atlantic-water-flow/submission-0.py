from collections import deque

class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
            p_que = deque()
            p_seen = set()

            a_que = deque()
            a_seen = set()

            rows, cols = len(heights), len(heights[0])

            for r in range(rows):
                p_que.append((r, 0))
                p_seen.add((r,0))
            
            
            for c in range(cols):
                p_que.append((0,c))
                p_seen.add((0,c))

            
            for r in range(rows):
                a_que.append((r, cols - 1))
                a_seen.add((r, cols - 1))


            for c in range(cols):
                a_que.append((rows - 1, c))
                a_seen.add((rows - 1, c ))


            def get_coords(que, seen):
                while que:
                    curr_x, curr_y = que.popleft()
                    for x_offset, y_offset in [(1,0), (-1,0), (0,1),(0,-1)]:
                            new_x,  new_y = curr_x + x_offset, curr_y + y_offset
                            if 0 <= new_x < rows and 0 <= new_y < cols and (new_x,new_y) not in seen and heights[new_x][new_y] >= heights[curr_x][curr_y]:
                                que.append((new_x, new_y))
                                seen.add((new_x, new_y))
            
            get_coords(p_que, p_seen)
            get_coords(a_que, a_seen)

            return list(p_seen.intersection(a_seen))
                        
