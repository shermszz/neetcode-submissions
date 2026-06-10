class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        # You want the k closest points, that means we want the k smallest in the heap
        # We should have a max Heap 
        maxHeap = [] # Should be of size k only

        def euclidean_dist(x1, y1):
            # no need to include x2, y2 since we are always comparing with the origin
            # We also don't need to include math.sqrt(), since if A > B, then √A > √B anyway
            return (x1 - 0) ** 2 + (y1 - 0) ** 2 # returns a double or float

        for i in range(len(points)):
            point = points[i]
            x, y = point[0], point[1]
            dist = euclidean_dist(x, y)
            if len(maxHeap) < k:
                heapq.heappush(maxHeap, (-dist, i, point)) # Push a tuple with (distance, index (in case of tiebreaker), the actual point) into the min heap
            else:
                if -dist > maxHeap[0][0]:
                    # We have found a dist value closer to 0, so we can kick out the current "maximum"
                    heapq.heappushpop(maxHeap, (-dist, i, point))
        # Now, extract all the points into a result list
        result = []
        while maxHeap:
            dist, index, point = heapq.heappop(maxHeap)
            result.append(point)
        return result

"""
=========================================================
KEY LEARNINGS: K Closest Points to Origin (LeetCode 973)
=========================================================

CORE CONCEPTS:
1. Max Heap for "K Smallest": To find the K closest/smallest 
   items in a stream, use a Max Heap of size K. The largest of 
   the K items sits at the root, ready to be kicked out.
2. The Square Root Optimization: When comparing Euclidean 
   distances, never compute the actual square root. Just 
   compare `x^2 + y^2`. Integer math is faster and safer 
   than floating-point math.
3. Python Tie-Breakers: If pushing tuples into a heap, include 
   a unique integer (like the index `i`) before any uncomparable 
   data types (like lists/objects) to prevent crash on tied values.

GUIDING HINTS:
- Remember that `heapq` is a Min Heap. Fake a Max Heap by 
  pushing `-dist`.
- When comparing against the root of a faked Max Heap, 
  remember that negatives flip inequalities! `new_dist < old_dist` 
  becomes `-new_dist > -old_dist`.
=========================================================
"""