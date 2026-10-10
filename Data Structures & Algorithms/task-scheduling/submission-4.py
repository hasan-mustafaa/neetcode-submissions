from collections import Counter, deque
import heapq
class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        count = Counter(tasks)
        heap = list(count.values())
        heapq.heapify_max(heap)
        time = 0
        queue = deque()

        while heap or queue:
            time += 1

            if heap:
                task_count = heapq.heappop_max(heap) - 1
                if task_count:
                    queue.append([task_count, time + n])
        
            if queue and queue[0][1] == time:
                updated_freq = queue.popleft()[0]
                heapq.heappush_max(heap, updated_freq)
        
        return time

            
