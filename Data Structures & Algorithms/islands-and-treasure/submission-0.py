class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        rows = len(grid)
        cols = len(grid[0])

        queue = deque()

        # Add every treasure chest to the queue
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 0:
                    queue.append((r, c))

        directions = [
            (1, 0),   # down
            (-1, 0),  # up
            (0, 1),   # right
            (0, -1)   # left
        ]

        while queue:
            r, c = queue.popleft()

            for dr, dc in directions:
                new_r = r + dr
                new_c = c + dc

                # Check whether the new cell is inside the grid
                if (
                    new_r < 0
                    or new_r >= rows
                    or new_c < 0
                    or new_c >= cols
                ):
                    continue

                # Only visit untouched land cells
                if grid[new_r][new_c] != 2147483647:
                    continue

                # Neighbor is one step farther away
                grid[new_r][new_c] = grid[r][c] + 1

                queue.append((new_r, new_c))