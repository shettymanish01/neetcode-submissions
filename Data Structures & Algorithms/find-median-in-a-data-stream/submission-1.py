class MedianFinder:

    def __init__(self):
        self.small = []
        self.large = []

    def addNum(self, num: int) -> None:
        if self.large and self.large[0] <= num:
            heapq.heappush(self.large, num)
        else:
            heapq.heappush(self.small, -1 * num)

        if len(self.large) > len(self.small) + 1:
            dig = heapq.heappop(self.large) * -1
            heapq.heappush(self.small, dig)
        elif len(self.small) > len(self.large) + 1:
            dig = heapq.heappop(self.small) * -1
            heapq.heappush(self.large, dig)
        

    def findMedian(self) -> float:
        if len(self.small) > len(self.large):
            return -1 * self.small[0]
        elif len(self.large) > len(self.small):
            return self.large[0]
        else:
            return ((self.small[0] * -1) + self.large[0]) / 2.0
        