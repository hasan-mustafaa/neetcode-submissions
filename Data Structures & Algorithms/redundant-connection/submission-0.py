class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        parents = [i for i in range(len(edges)+ 1)]
        rank = [1] * (len(edges) + 1)
        redundant_connection = 0
        

        def find(node):

            while node != parents[node]:
                parents[node] = parents[parents[node]]
                node = parents[node]
            
            return node
        
        def union(node1,node2):
            parent1, parent2 = find(node1), find(node2)
            nonlocal redundant_connection 

            if parent1 == parent2:
                redundant_connection = [node1, node2]
                return
            
            if rank[parent1] > rank[parent2]:
                parents[parent2] = parent1
                rank[parent1] += rank[parent2]
            else:
                parents[parent1] = parent2
                rank[parent2] += rank[parent1]
            
        
        for n1,n2 in edges:
            res = union(n1,n2)

        return redundant_connection

