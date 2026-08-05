class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        
        graph = {i : [] for i in range(1, len(edges) + 1)}

        def hasPath(node, target, visit):

            if node == target:
                return True

            visit.add(node)

            for neighbor in graph[node]:
                if neighbor not in visit:
                    if hasPath(neighbor, target, visit):
                        return True
            
            return False 

        
        for u, v in edges:
            if hasPath(u, v, set()):
                return [u, v]
            
            graph[u].append(v)
            graph[v].append(u)

        