class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        n = len(points)
        node = 0
        dist = [100000000] * n
        visit = [False] * n
        edges = 0
        res = 0

        while edges < n - 1:
            visit[node] = True
            nextNode = -1

            for i in range(n):
                if visit[i] == True:
                    continue
                curDist = abs(points[i][0] - points[node][0]) + abs(points[i][1] - points[node][1])
                dist[i] = min(dist[i], curDist)
                if nextNode == -1 or dist[i] < dist[nextNode]:
                    nextNode = i

            res += dist[nextNode]
            edges += 1
            node = nextNode
        return res
