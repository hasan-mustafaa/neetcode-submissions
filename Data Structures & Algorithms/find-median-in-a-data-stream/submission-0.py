class MedianFinder:

    def __init__(self):
        self.small = []
        self.large = []
        

    def addNum(self, num: int) -> None:
        heapq.heappush_max(self.small, num)
        heapq.heappush(self.large, heapq.heappop_max(self.small))

        if len(self.large) > len(self.small):
            heapq.heappush_max(self.small, heapq.heappop(self.large))
        

    def findMedian(self) -> float:
        """
        handle odd and even case
        if len is odd, we do len // 2 - 1 pops and return the next one
        else if even, 
        """
        if len(self.small) - len(self.large) == 1:
            return self.small[0]
        else:
            return (self.small[0] + self.large[0]) / 2 
        