class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        
        #Note, we use n + 1 everywhere, as people are 1-index
        labels = n + 1

        out_edges = [[] for i in range(labels)]
        indegree = [0] * (labels)

        for u, v in trust:
            out_edges[u].append(v)
            indegree[v] += 1

        for i in range(1, labels):
            #Town Judge doesn't vote for himself
            # out_edges[i] == [], considered falsy hence not out_edges
            if not out_edges[i] and indegree[i] == n - 1:
                return i
        return -1

    
    """
    Fulfill Conditions:
    1. No outgoing edges, outedges[u] == []
    1. Incoming edges = n - 1 (Town Judge himself)
    """
        

        
