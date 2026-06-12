class MedianFinder:

    def __init__(self): 
        self.minHeap = [] # To get the smallest of the big numbers
        self.maxHeap = [] # To get the biggest of the small numbers

    def addNum(self, num: int) -> None:
        # Always throw the number into the maxHeap first. 
        heapq.heappush(self.maxHeap, -num)

        # Then, throw into the minHeap
        heapq.heappush(self.minHeap, -heapq.heappop(self.maxHeap))

        if len(self.minHeap) - len(self.maxHeap) > 1:
            # Throw the top element back to the maxHeap
            heapq.heappush(self.maxHeap, -heapq.heappop(self.minHeap))

    def findMedian(self) -> float:
        # In my case, if there are odd number of values, the minHeap is holding the median value
        if len(self.minHeap) != len(self.maxHeap):
            # Median for sure in minHeap
            return self.minHeap[0] / 1
        else:
            median = (self.minHeap[0] + -1 * self.maxHeap[0]) / 2
            return median
        
"""
=========================================================
KEY LEARNINGS: Find Median from Data Stream (LeetCode 295)
=========================================================

CORE CONCEPTS:
1. The Two-Heap Paradigm: To instantly access the middle of a 
   sorted dataset, slice it in half. 
   - Lower Half = Max-Heap (Finds the biggest small number)
   - Upper Half = Min-Heap (Finds the smallest big number)
2. The Bouncer Hand-off: Never try to guess which heap a number 
   belongs to. Throw every number into Heap A, immediately pop 
   Heap A's top, and throw it into Heap B. 
3. The Size Balancer: If Heap B gets too big (size difference > 1), 
   pop its top and throw it back to Heap A. 

GUIDING HINTS:
- In Python, `heapq` is a Min-Heap. Fake your Max-Heap by pushing 
  negative numbers (`-num`). 
- When calculating the median from the Max-Heap, never forget to 
  multiply by `-1` to restore the true value!
- Whichever heap you route numbers to LAST in your `addNum` logic 
  is the heap that will hold the extra element when the count is odd.
=========================================================
"""
        