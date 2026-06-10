class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        neg_stones = [-s for s in stones]
        heapq.heapify(neg_stones) # now neg_stones is a max_heap

        while len(neg_stones) > 1:
            x, y = -heapq.heappop(neg_stones), -heapq.heappop(neg_stones)
            if x > y:
                diff = x - y
                heapq.heappush(neg_stones, -diff) # Keep stone x with reduced weight
            # Otherwise destroy both
        
        return -1 * neg_stones[0] if neg_stones else 0
    
"""
=========================================================
KEY LEARNINGS: Last Stone Weight (LeetCode 1046)
=========================================================

CORE CONCEPTS:
1. Max Heaps in Python: Python's `heapq` only implements Min Heaps. 
   To create a Max Heap, multiply all values by -1, push them, and 
   multiply by -1 again when popping.
2. Heap Properties: The first item popped from a Max Heap is ALWAYS 
   the largest. `first >= second` is a mathematical guarantee.

GUIDING HINTS:
- Be careful with `while len != 1`. In games of elimination, 
  collections can drop by 2 elements at once, skipping 1 and 
  landing on 0. Always use `while len > 1`.
- Time Complexity: O(N) to heapify + O(N log N) for the while loop.
- Space Complexity: O(N) for the heap.
=========================================================
"""