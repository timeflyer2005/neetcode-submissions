class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        rows = len(matrix)
        cols = len(matrix[0])

        first_row_has_zero = False
        first_col_has_zero = False

        # Check whether the first row originally has a zero
        for col in range(cols):
            if matrix[0][col] == 0:
                first_row_has_zero = True

        # Check whether the first column originally has a zero
        for row in range(rows):
            if matrix[row][0] == 0:
                first_col_has_zero = True

        # Use the first row and first column as markers
        for row in range(1, rows):
            for col in range(1, cols):
                if matrix[row][col] == 0:
                    matrix[row][0] = 0
                    matrix[0][col] = 0

        # Use the markers to update the inside of the matrix
        for row in range(1, rows):
            for col in range(1, cols):
                if matrix[row][0] == 0 or matrix[0][col] == 0:
                    matrix[row][col] = 0

        # Update the first row last
        if first_row_has_zero:
            for col in range(cols):
                matrix[0][col] = 0

        # Update the first column last
        if first_col_has_zero:
            for row in range(rows):
                matrix[row][0] = 0