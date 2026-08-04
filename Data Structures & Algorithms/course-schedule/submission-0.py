class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:

        # prereq_map[course] = prerequisites needed for that course
        prereq_map = {course: [] for course in range(numCourses)}

        for course, prereq in prerequisites:
            prereq_map[course].append(prereq)

        visiting = set()

        def dfs(course):
            # We reached the same course again in the current path
            if course in visiting:
                return False
        
            # No prerequisites left to check
            if prereq_map[course] == []:
                return True

            visiting.add(course)

            for prereq in prereq_map[course]:
                if not dfs(prereq):
                    return False

            visiting.remove(course)

            # Mark this course as already verified
            prereq_map[course] = []

            return True

        for course in range(numCourses):
            if not dfs(course):
                return False

        return True