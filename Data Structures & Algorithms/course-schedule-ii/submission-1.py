class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        
        graph = {i: [] for i in range(numCourses)}
        indegree = [0] * numCourses

        for course, prereq in prerequisites:
            graph[prereq].append(course)
            indegree[course] += 1
        
        queue = deque()
        
        for course in range(numCourses):
            if indegree[course] == 0:
                queue.append(course)
        
        course_taken = 0
        res = []
        while queue:

            course = queue.popleft()
            course_taken += 1
            res.append(course)

            for next_course in graph[course]:
                indegree[next_course] -= 1
                
                if indegree[next_course] == 0:
                    queue.append(next_course)
    
        if course_taken == numCourses:
            return res
        return []
            