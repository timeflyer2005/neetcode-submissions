from collections import defaultdict, deque

class Solution:
    def foreignDictionary(self, words):
        graph = defaultdict(set)
        indegree = {}

        # Add every character to indegree
        for word in words:
            for char in word:
                indegree[char] = 0

        # Compare adjacent words
        for i in range(len(words) - 1):
            word1 = words[i]
            word2 = words[i + 1]

            minLen = min(len(word1), len(word2))

            # Invalid case: ["abc", "ab"]
            if len(word1) > len(word2) and word1[:minLen] == word2[:minLen]:
                return ""

            # Find first different character
            for j in range(minLen):
                if word1[j] != word2[j]:
                    c1 = word1[j]
                    c2 = word2[j]

                    # c1 must come before c2
                    if c2 not in graph[c1]:
                        graph[c1].add(c2)
                        indegree[c2] += 1

                    break

        # Topological sort
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

        # Cycle exists
        if len(result) != len(indegree):
            return ""

        return "".join(result)