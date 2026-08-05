class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        
        graph = {i : [] for i in range(n)}

        for n1, n2 in edges:
            graph[n1].append(n2)
            graph[n2].append(n1)

        visit = set()
        count = 0

        def dfs(node):

            if node in visit:
                return
            
            visit.add(node)

            for neighbor in graph[node]:
                dfs(neighbor)
            
        
        for node in range(n):
            if node not in visit:
                dfs(node)
                count += 1
        return count
                
            