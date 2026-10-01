class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        in_edges = defaultdict(list)
        out_edges = defaultdict(list)

        for course, prereq in prerequisites:
            in_edges[course].append(prereq)
            out_edges[prereq].append(course)

        canTake = [i for i in range(numCourses) if len(in_edges[i]) == 0]
        taken = []

        while canTake:
            currCourse = canTake.pop()
            taken.append(currCourse)
            for nextCourse in out_edges[currCourse]:
                in_edges[nextCourse].remove(currCourse)
                if len(in_edges[nextCourse]) == 0:
                    canTake.append(nextCourse)
        
        return taken if len(taken) == numCourses else []