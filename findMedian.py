import sys
import heapq
class MedianFinder:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.maxheap=[]
        self.minheap=[]
        self.median=-sys.maxint-1


    def addNum(self, num):
        """
        Adds a num into the data structure.
        :type num: int
        :rtype: void
        """

        heapq.heappush(self.maxheap, -num)
        t=heapq.heappop(self.maxheap)

        heapq.heappush(self.minheap, -t)

        if len(self.minheap) > len(self.maxheap):
            x=heapq.heappop(self.minheap)
            heapq.heappush(self.maxheap, -x)




    def findMedian(self):
        """
        Returns the median of current data stream
        :rtype: float
        """
        m, n=len(self.maxheap), len(self.minheap)
        if m==n: return float((-self.maxheap[0]+self.minheap[0])/2.0)
        elif m>n: return float(-self.maxheap[0])
        elif n>m: return float(self.minheap[0])
