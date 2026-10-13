class Solution:
    def kClosest(self, points: list[list[int]], k: int) -> list[list[int]]:
        """
            GOAL: Return the k closest points to the origin
            That signals that we have to use a heap.
            - We probably want to use a max heap because we want the k closest poitns, meaning the values we want to keep are the smallest ones
            - We want to remove all the big ones, so we maintain a max_heap so that we can easily pop the biggest ones when comparing what points to keep

            Idea:
                - We are given a list of points (x, y), make them into a tuple first so we can store them into a max_heap
                - add an additional element to the point (euclidean dist, x, y). Since we are comparing the distance from (0, 0), then the euclidean distance is simply sqrt(x**2 - y**2)
                - Then, when we push to the max_heap, we need to push the negative version of the euclidean distance, since it is default a min_heap

                - We push as long as the size of the max_heap hasnt exceeded size k.
                - If already size k, then we compare. The value whose euclidean distnance is smaller should be inside the maxheap (the more negative version should be removed)
        """

        max_heap = []
        n = len(points)

        for i in range(n):
            x, y = points[i]
            neg_eu_dist = -1 * (x**2 + y**2) 
            if len(max_heap) < k:
                # 1. Easy case, just keep adding the point into the max_heap
                heapq.heappush(max_heap, (neg_eu_dist, x, y))
            else:
                # 2. There are already k elements inside the list, so we need to remove the most negative one
                # If the current value in the heap is MORE NEGATIVE than the one we are inspecting now, we will pop the heap point
                if max_heap[0][0] < neg_eu_dist:
                    heapq.heappop(max_heap)
                    heapq.heappush(max_heap, (neg_eu_dist, x, y))
        
        # Now we have k points inside our heap, we just need to go through each one and print it as a list without their distances
        res = []
        for _, x, y in max_heap:
            res.append([x, y])
        return res
