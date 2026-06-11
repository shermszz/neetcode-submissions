class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        heapq.heapify(nums) # now nums is a min_heap
        # The min heap should only contain k elements
        while len(nums) > k: # This is good only when k is large., otherwise degenerates to NlogN solution
            heapq.heappop(nums) 
        return nums[0]
    