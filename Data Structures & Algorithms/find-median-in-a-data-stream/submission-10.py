class MedianFinder:

    def __init__(self):
        self.large, self.small = [], []

    def addNum(self, num: int) -> None:
        if self.large and num <= (self.large[0] * -1):
            heapq.heappush(self.large,-1 * num)
        else:
            heapq.heappush(self.small, num)
        
        if len(self.large) - len(self.small) > 1:
            heapq.heappush(self.small, -1 * heapq.heappop(self.large))
        elif len(self.small) - len(self.large) > 1:
            heapq.heappush(self.large, -1 * heapq.heappop(self.small))

    def findMedian(self) -> float:
        print(self.small, self.large)
        if len(self.large) > len(self.small):
            return self.large[0] * -1

        if len(self.small) > len(self.large):
            return self.small[0]
        
        return (self.small[0] + (-1 * self.large[0])) / 2
        
        