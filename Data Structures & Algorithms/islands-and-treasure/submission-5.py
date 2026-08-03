class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        row = len(grid)
        col = len(grid[0])

        queue = deque()

        for r in range(row):
            for c in range(col):
                if grid[r][c] == 0:
                    queue.append((r,c))

        
        directions = [
            [1, 0],
            [0, 1],
            [-1, 0],
            [0, -1]
        ]

        while queue:
            r, c = queue.popleft()

            for dr, dc in directions:
                new_r = r + dr
                new_c = c + dc

                if new_r < 0 or new_r >= row or new_c < 0 or new_c >= col or grid[new_r][new_c] != 2147483647:
                    continue
                
                grid[new_r][new_c] = grid[r][c] + 1

                queue.append((new_r, new_c))
            
            