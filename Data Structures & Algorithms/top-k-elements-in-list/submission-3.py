class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        """
        GOAL: Return the k most frequent elements in the array
        e.g. = [1, 2, 2, 3, 3, 3] and k = 2
            - We want to return the 2 most frequent elements.
            - That means we want to return [2, 3] because 2 has a count of 2, 3 has a count of 3
        
        One data structure we can use is a min heap
            - We can keep it to the size of k
            - If the heap is not yet size == k: we add the value into the heap
            - If the heap is already size == k:
                We need to check what is the count of the element that we want to add VS min_heap count
                if min_heap count is < count of curr element
                    - Then we pop the from the min_heap and then push the current element into the heap

        Now what do we add into the heap? 
            - We ideally want to have the (count, number) inside and the minheap will sort based on the count
            - To get the count, we would need to do an initial pass on nums to get the total frequency of each value to be stored inside a hash map
            - Then from the hashmap, we will iterate through its items() and then store them into the minHeap
        """

        min_heap = [] # To be strictly size k only
        my_map = Counter(nums) # Which has the frequencies of all distinct values 

        # Now we iterate across the hashmap
        for val, freq in my_map.items():
            if len(min_heap) < k:
                heapq.heappush(min_heap, (freq, val)) # Push the tuple inside
            else:
                # Once we hit the size of the min_heap, we need to figure out which element to remove now
                # We can easily compare the smallest one that is at the top of the min_heap
                if freq > min_heap[0][0]:
                    # The frequency we about to add is bigger than the min_heap smallest value, so we evict the top value inside the min_heap
                    heapq.heappop(min_heap)
                    heapq.heappush(min_heap, (freq, val))
        # At the end, we have a min_heap of k values that appeared the most
        return [val for _ , val in min_heap]
    




