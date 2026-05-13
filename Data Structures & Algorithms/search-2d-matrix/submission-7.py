class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        #Matrix is in increasing order
        rows = len(matrix) 
        columns = len(matrix[0])
        left = 0
        right = rows * columns - 1

        while left <= right:
            middle = (right + left) // 2
            row = middle // columns
            column = middle % columns

            if matrix[row][column] == target:
                return True
            elif matrix[row][column] < target:
                left = middle + 1
            else:
                right = middle - 1

        return False