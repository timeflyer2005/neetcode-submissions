class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:

        graph = {}

        for i in range(numCourses):
            graph[i] = []
        
        for course, prereq in prerequisites:
            graph[course].append(prereq)
        
        visit = set()

        def dfs(course):

            if course in visit:
                return False
            
            if graph[course] == []:
                return True
            
            visit.add(course)

            for prereq in graph[course]:
                if not dfs(prereq):
                    return False
            
            visit.remove(course)
            graph[course] = []

            return True
        
        for course in range(numCourses):
            if not dfs(course):
                return False
        return True

        