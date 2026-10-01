class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
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