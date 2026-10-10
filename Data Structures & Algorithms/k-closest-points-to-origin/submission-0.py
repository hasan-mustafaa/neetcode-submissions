import math
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        res = []
        distance = []

        for x,y in points:
            distance.append((x**2 + y**2, x, y))
        
        heapq.heapify(distance)

        for i in range(k):
            d, x, y = heapq.heappop(distance)
            res.append([x,y])
        
        return res


