class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        # We need to have the kth largest element to be the root of the heap
        # We should be using a minHeap of size K, let the larger elements sink to the bottom
        self.minHeap = []
        self.maxSize = k
        for num in nums:
            self.add(num)

    def add(self, val: int) -> int:
        # We want to always return the kth largest element, which is the root of the 
        if len(self.minHeap) == self.maxSize and val > self.minHeap[0]:
                # We have hit the limit, need to evict an element from the minHeap
                # Who to evict?  --> Just the smallest element
                heapq.heappop(self.minHeap)
                heapq.heappush(self.minHeap, val)
        elif len(self.minHeap) < self.maxSize:
            heapq.heappush(self.minHeap, val)
        return self.minHeap[0]


