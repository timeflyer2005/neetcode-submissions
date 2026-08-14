class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        graph = defaultdict(list)
        
        for fromi, toi in tickets:
            heapq.heappush(graph[fromi], toi)
        
        route = []
        def dfs(airport):

            while graph[airport]:
                destination = heapq.heappop(graph[airport])
                dfs(destination)
            route.append(airport)

        dfs("JFK")
        return route[::-1]
