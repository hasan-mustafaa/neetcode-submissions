from collections import deque
class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        out_edges = [[] for i in range(numCourses)]
        indegree = [0] * numCourses

        for course, prereq in prerequisites:
            out_edges[prereq].append(course)
            indegree[course] += 1
        
        que = deque([course for course in range(numCourses) if indegree[course] == 0])
        order = []

        while que:
            course_taken = que.pop()
            order.append(course_taken)

            for nxt in out_edges[course_taken]:
                indegree[nxt] -= 1
                if indegree[nxt] == 0:
                    que.append(nxt)
        
        return order if len(order) == numCourses else []