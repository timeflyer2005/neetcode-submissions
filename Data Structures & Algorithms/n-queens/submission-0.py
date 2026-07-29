class Solution:
    def solveNQueens(self, n: int) -> list[list[str]]:
        result = []

        board = [["."] * n for _ in range(n)]

        columns = set()
        negative_diagonals = set()  # row - column
        positive_diagonals = set()  # row + column

        def backtrack(row: int) -> None:
            # We successfully placed a queen in every row
            if row == n:
                solution = ["".join(board_row) for board_row in board]
                result.append(solution)
                return

            # Try every column in this row
            for column in range(n):
                if (
                    column in columns
                    or row - column in negative_diagonals
                    or row + column in positive_diagonals
                ):
                    continue

                # Place queen
                board[row][column] = "Q"
                columns.add(column)
                negative_diagonals.add(row - column)
                positive_diagonals.add(row + column)

                # Move to the next row
                backtrack(row + 1)

                # Remove queen
                board[row][column] = "."
                columns.remove(column)
                negative_diagonals.remove(row - column)
                positive_diagonals.remove(row + column)

        backtrack(0)
        return result