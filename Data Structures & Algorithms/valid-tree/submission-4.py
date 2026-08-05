class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:

        # A tree with n nodes must have exactly n - 1 edges
        if len(edges) != n - 1:
            return False

        graph = {i: [] for i in range(n)}

        for a, b in edges:
            graph[a].append(b)
            graph[b].append(a)

        visit = set()
        queue = deque([(0, -1)])   # (node, parent)

        while queue:
            node, parent = queue.popleft()

            if node in visit:
                return False

            visit.add(node)

            for neighbor in graph[node]:
                if neighbor == parent:
                    continue
                queue.append((neighbor, node))

        return len(visit) == n