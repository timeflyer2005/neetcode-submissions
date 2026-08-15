class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        
        graph = [[] for _ in range(n)]

        for u, v, price in flights:
            graph[u].append((v, price))
        
        minHeap = [(0, src, 0)]
        best = [[float("infinity")] * (k + 2) for _ in range(n)]

        best[src][0] = 0

        while minHeap:

            cost, node, flight_used = heapq.heappop(minHeap)

            if cost > best[node][flight_used]:
                continue

            if node == dst:
                return cost
            
            if flight_used == k + 1:
                continue 
            
            for neighbor, price in graph[node]:
                
                newCost = cost + price
                newFlight = flight_used + 1

                if newCost < best[neighbor][newFlight]:
                    best[neighbor][newFlight] = newCost
                    heapq.heappush(minHeap, (newCost, neighbor, newFlight))
        
        return -1
                    
                
            
            