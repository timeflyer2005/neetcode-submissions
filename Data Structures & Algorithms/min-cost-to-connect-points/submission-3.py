class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        node = 0
        n = len(points)
        dist = [10000000] * n
        visited = [False] * n
        edges = 0
        res = 0

        while edges < n - 1:
            visited[node] = True
            nextNode = -1

            for i in range(n):
                if visited[i]:
                    continue
                
                curdist = abs(points[i][0] - points[node][0]) + abs(points[i][1] - points[node][1])

                dist[i] = min(dist[i], curdist)

                if nextNode == -1 or dist[i] < dist[nextNode]:
                    nextNode = i
            
            res += dist[nextNode]
            node = nextNode
            edges += 1
        return res