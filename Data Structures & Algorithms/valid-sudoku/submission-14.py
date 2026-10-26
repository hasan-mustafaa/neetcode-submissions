class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = [set() for i in range(9)]
        cols = [set() for i in range(9)]
        box = [set() for i in range(9)]


        for r in range(9):
            for c in range(9):
                cell_val = board[r][c]
                if cell_val == ".": continue
                if cell_val in rows[r]: return False
                rows[r].add(cell_val)
                if cell_val in cols[c]: return False
                cols[c].add(cell_val)
                boxes = (r // 3) * 3 + (c // 3)
                if cell_val in box[boxes]: return False
                box[boxes].add(cell_val)
            
        
        return True
                