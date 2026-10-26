import heapq
from collections import Counter
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = Counter(nums)
        heap = []
        res = []

        for num, count in count.items():
            heapq.heappush_max(heap, (count, num))

        for i in range(k):
            count, num = heapq.heappop_max(heap)
            res.append(num)
        
        return res

        