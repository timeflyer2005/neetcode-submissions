class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:        
        row = len(grid)
        col = len(grid[0])

        queue = deque()
        fresh = 0

        for r in range(row):
            for c in range(col):
                if grid[r][c] == 2:
                    queue.append((r, c))
                elif grid[r][c] == 1:
                    fresh += 1 


        directions = [
            [1, 0],
            [-1, 0],
            [0, 1],
            [0, -1]
        ]
        minutes = 0
        while queue and fresh > 0:
            for _ in range(len(queue)):
                r, c = queue.popleft()
                for dr, dc in directions:
                    new_r = r + dr
                    new_c = c + dc

                    if new_r < 0 or new_r >= row or new_c < 0 or new_c >= col:
                        continue
                    if grid[new_r][new_c] != 1:
                        continue
                    
                    grid[new_r][new_c] = 2
                    fresh -= 1
                    queue.append((new_r, new_c))
            
            minutes += 1
        
        if fresh == 0:
            return minutes
        return -1