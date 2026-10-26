
from collections import defaultdict
import heapq
class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        edges = defaultdict(list)

        for u, v, w in times: #Use populated edge list
            edges[u].append((w, v)) #Make sure weight is first

        minHeap = [(0, k)]
        visited = set()
        total_time = 0

        while minHeap:
            dist, node = heapq.heappop(minHeap)

            if node in visited:
                continue #Don't return
            
            visited.add(node)
            total_time = dist

            for dist2, node2 in edges[node]:
                if node2 not in visited:
                    new_dist = dist + dist2
                    heapq.heappush(minHeap, (new_dist, node2))
        

        return total_time if len(visited) == n else -1
        




            