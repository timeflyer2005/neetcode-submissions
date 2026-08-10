class Solution:
    def networkDelayTime(self, times, n, k):
        graph = {i: [] for i in range(1, n + 1)}

        for u, v, w in times:
            graph[u].append((v, w))

        minHeap = [(0, k)]
        visit = set()
        total_time = 0

        while minHeap:
            
            w1, node = heapq.heappop(minHeap)

            if node in visit:
                continue
            
            visit.add(node)

            total_time = w1

            for neighbor, weight in graph[node]:
                if neighbor not in visit:
                    heapq.heappush(minHeap, (weight + w1, neighbor))
        
        return total_time if len(visit) == n else -1

        

