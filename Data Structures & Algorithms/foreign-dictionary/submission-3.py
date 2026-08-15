class Solution:
    def foreignDictionary(self, words: List[str]) -> str:
        graph = defaultdict(set)
        indegree = {}


        for word in words:
            for char in word:
                indegree[char] = 0
        
        for i in range(len(words) - 1):
            word1 = words[i]
            word2 = words[i + 1]
            
            minLen = min(len(word1), len(word2))

            if len(word1) > len(word2) and word1[:minLen] == word2[:minLen]:
                return ""
            
            for j in range(minLen):
                if word1[j] != word2[j]:
                    c1 = word1[j]
                    c2 = word2[j]

                    if c2 not in graph[c1]:
                        graph[c1].add(c2)
                        indegree[c2] += 1

                    break
        
        queue = deque()

        for char in indegree:
            if indegree[char] == 0:
                queue.append(char)
                
        result = []

        while queue:
            char = queue.popleft()
            result.append(char)

            for neighbor in graph[char]:
                indegree[neighbor] -= 1
                
                if indegree[neighbor] == 0:
                    queue.append(neighbor)
                
        if len(result) != len(indegree):
            return ""

        return "".join(result)
            
            
        
        