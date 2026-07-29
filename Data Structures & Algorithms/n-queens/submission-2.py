class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        
        result = []
        board = [["."] * n for _ in range(n)]
        columns = set()
        negative_diagonals = set()
        positive_diagonals = set()

        def backtrack(row):

            if row == n:
                solution = ["".join(board_row) for board_row in board]
                result.append(solution)
                return
            
            for column in range(n):
                if (
                    column in columns
                    or row - column in negative_diagonals
                    or row + column in positive_diagonals
                ):
                    continue 

                board[row][column] = "Q"
                columns.add(column)
                negative_diagonals.add(row - column)
                positive_diagonals.add(row + column)

                backtrack(row + 1)

                board[row][column] = "."
                columns.remove(column)
                negative_diagonals.remove(row - column)
                positive_diagonals.remove(row + column)
        backtrack(0)

        return result
            
        