class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        parents = [i for i in range(n)]
        rank = [1] * n

        def find(node):
            while node != parents[node]:
                parents[node] = parents[parents[node]]
                node = parents[node]
            return node
        
        def union(node1,node2):
            parent1, parent2 = find(node1), find(node2)

            if parent1 == parent2:
                return 0

            if rank[parent2] > rank[parent1]:
                parents[parent1] = parent2
                rank[parent2] += rank[parent1]
            else:
                parents[parent2] = parent1
                rank[parent1] += rank[parent2]
            return 1


        
        res = n
        for node1, node2 in edges:
            res -= union(node1,node2)
        return res