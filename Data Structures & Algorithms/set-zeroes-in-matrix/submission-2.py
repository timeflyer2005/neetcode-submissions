class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        
        zero_row = set()
        zero_col = set()

        row = len(matrix)
        col = len(matrix[0])

        for r in range(row):
            for c in range(col):
                if matrix[r][c] == 0:
                    zero_row.add(r)
                    zero_col.add(c)

        for r in range(row):
            for c in range(col):
                if r in zero_row or c in zero_col:
                    matrix[r][c] = 0