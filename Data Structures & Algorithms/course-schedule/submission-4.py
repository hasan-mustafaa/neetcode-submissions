from collections import deque
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        out_edges = [[] for i in range(numCourses)]
        indegree = [0] * numCourses

        for course, prereq in prerequisites:
            out_edges[prereq].append(course)
            indegree[course] += 1
        
        que = deque([course for course in range(numCourses) if indegree[course] == 0])
        courses_taken = 0

        while que:
            course = que.popleft()
            courses_taken += 1

            for nxt in out_edges[course]:
                indegree[nxt] -= 1
                if indegree[nxt] == 0:
                    que.append(nxt)
        
        return courses_taken == numCourses



    