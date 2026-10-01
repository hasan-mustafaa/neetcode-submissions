class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        parents = [i for i in range(n)]
        rank = [1] * n

        if len(edges) != n - 1:
            return False
            
        def find(node):
            while node != parents[node]:
                parents[node] = parents[parents[node]]
                node = parents[node]     
            return node

        
        def union(node1, node2):
            parent1, parent2 = find(node1), find(node2)

            if parent1 == parent2:
                return False
            
            if rank[parent1] > rank[parent2]:
                parents[parent2] = parent1
                rank[parent1] += rank[parent2]
            else:
                parents[parent1] = parent2
                rank[parent2] += rank[parent1]
            
            return True
            
        for n1,n2 in edges:
            if not union(n1,n2):
                return False
        
        return True

