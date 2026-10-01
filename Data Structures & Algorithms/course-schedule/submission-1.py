class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        in_edges = defaultdict(list)
        out_edges = defaultdict(list)

        for course, prereq in prerequisites:
            in_edges[course].append(prereq)
            out_edges[prereq].append(course)
        
        canTake = [i for i in range(numCourses) if len(in_edges[i]) == 0]
        taken = 0

        while canTake:
            curr_course = canTake.pop()
            taken += 1
            for nextCourse in out_edges[curr_course]:
                in_edges[nextCourse].remove(curr_course)
                if len(in_edges[nextCourse]) == 0:
                    canTake.append(nextCourse)
        
        return taken == numCourses

        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        """
        prereq_of = defaultdict(list)

        for course, prereq in prerequisites:
            prereq_of[course].append(prereq)

        UNVISITED = 0
        VISITING = 1
        VISITED = 2
        states = [UNVISITED] * numCourses
        
        def dfs(node):
            state = states[node]

            if state == VISITED: return True
            elif state == VISITING: return False

            states[node] = VISITING

            for neighbors in prereq_of[node]:
                if not dfs(neighbors):
                    return False

            states[node] = VISITED
            return True

        
        for i in range(numCourses):
            if not dfs(i):
                return False
        
        return True
        """