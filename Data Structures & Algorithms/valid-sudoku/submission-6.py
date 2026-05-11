class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = [set() for r in range(9)]
        columns = [set() for c in range(9)]
        boxes = [set() for b in range(9)]

        for row in range(9):
            for column in range(9):
                if board[row][column] == '.':
                    continue
                if board[row][column] in rows[row]:
                    return False
                rows[row].add(board[row][column])
                if board[row][column] in columns[column]:
                    return False
                columns[column].add(board[row][column]) 
                box_index = (row // 3) * 3 + (column // 3)
                if board[row][column] in boxes[box_index]:
                    return False
                boxes[box_index].add(board[row][column])
        return True
