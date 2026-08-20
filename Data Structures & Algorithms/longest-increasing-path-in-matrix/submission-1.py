class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        
        rows = len(matrix)
        col = len(matrix[0])

        dp = {}

        def dfs(r, c):
            if (r, c) in dp:
                return dp[(r,c)]
            
            best = 1

            directions = [
                (1, 0),
                (-1, 0),
                (0, 1),
                (0, -1)
            ]

            for dr, dc in directions:
                nr = r + dr
                nc = c + dc

                if 0 <= nr < rows and 0 <= nc < col and matrix[nr][nc] > matrix[r][c]:
                    best = max(best, 1 + dfs(nr, nc))
            
            dp[(r, c)] = best
            return best
        
        ans = 0
        for r in range(rows):
            for c in range(col):
                ans = max(ans, dfs(r, c))
        return ans
