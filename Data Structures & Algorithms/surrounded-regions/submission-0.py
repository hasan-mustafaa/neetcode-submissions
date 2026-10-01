class Solution:
    def solve(self, board: List[List[str]]) -> None:
        rows, cols = len(board), len(board[0])
        stk = []

        for c in range(cols):
            if board[0][c] == 'O': stk.append((0,c))
            if rows > 1 and board[rows-1][c] == "O": stk.append((rows - 1, c))
        
        for r in range(1, rows):
            if board[r][0] == "O":stk.append((r, 0))
            if cols > 1 and board[r][cols - 1] == "O": stk.append((r, cols - 1))

        while stk:
            curr_row, curr_col = stk.pop()
            board[curr_row][curr_col] = "S"
            for r_offset, c_offset in [[1,0],[0,1],[-1,0],[0,-1]]:
                new_row = curr_row + r_offset
                new_col = curr_col + c_offset
                if (0 <= new_row < rows 
                    and 0<= new_col < cols 
                    and board[new_row][new_col] == "O"):
                    stk.append((new_row,new_col))
                    board[new_row][new_col] = "S"
        
        for r in range(rows):
            for c in range(cols):
                if board[r][c] == "S":
                    board[r][c] = "O"
                elif board[r][c] == "O":
                    board[r][c] = "X"


                