class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        n = len(grid)
        dist = [[1000000000] * n for _ in range(n)]
        visited = [[False] * n for _ in range(n)]
        dist[0][0] = grid[0][0]
        minHeap = [(grid[0][0], 0, 0)]

        directions = [
            (1, 0),
            (0, 1),
            (-1, 0),
            (0, -1)
        ]

        while minHeap:

            time, r, c = heapq.heappop(minHeap)

            if visited[r][c] == True:
                continue
            visited[r][c] = True
            
            if r == n - 1 and c == n - 1:
                return time
            
            for dr, dc in directions:

                nr = r + dr
                nc = c + dc

                if 0 <= nr < n and 0 <= nc < n and not visited[nr][nc]:
                    newTime = max(time, grid[nr][nc])
                    if newTime < dist[nr][nc]:
                        dist[nr][nc] = newTime
                        heapq.heappush(minHeap, (newTime, nr, nc))
            
        