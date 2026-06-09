class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.minHeap = nums
        self.maxSize = k
        heapq.heapify(self.minHeap) # Turns nums into a minHeap in O(N)

        while (len(self.minHeap) > k):
            heapq.heappop(self.minHeap)

    def add(self, val: int) -> int:
        if len(self.minHeap) < self.maxSize:
            heapq.heappush(self.minHeap, val)
        elif val > self.minHeap[0]:
            heapq.heappushpop(self.minHeap, val) # pushes first, then pops
            # Since we gurantee val is bigger than the current smallest element, the element popped is the smallest element that was previously inside the minHeap, and we will not pop the val we just pushed

        return self.minHeap[0]       

"""
=========================================================
KEY LEARNINGS: Kth Largest Element in a Stream (LeetCode 703)
=========================================================

CORE CONCEPTS:
1. The "Top K" VIP Club: Whenever a problem asks for the "Kth Largest" 
   of anything over time, use a Min Heap of size K. The smallest 
   element of the largest K elements will always be at the root.
2. Built-in Optimizations: 
   - `heapq.heapify(arr)` creates a heap in O(N) time.
   - `heapq.heappushpop(heap, val)` is faster than a pop followed by a push.

COMPLEXITY:
- Initialization Time: O(N) to heapify + O((N-k) * log N) to pop down to k.
- Add Time: O(log k)
- Space: O(k) for the heap.
=========================================================
"""
