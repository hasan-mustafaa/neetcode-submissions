class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        out_edges = [[] for i in range(n + 1)]
        indegree = [0] * (n + 1)

        for u, v in trust:
            out_edges[u].append(v)
            indegree[v] += 1

        for i in range(1, n + 1):
            if out_edges[i] == [] and indegree[i] == n - 1:
                return i
        return -1

    
    """
    Fulfill Conditions:
    1. No outgoing edges, outedges[u] == []
    1. Incoming edges = n - 1 (Town Judge himself)
    """
        

        
