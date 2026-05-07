class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # First, set a dictonary to have the number itself as key, value is the frequency of the key
        myMap = defaultdict(int)
        for num in nums:
            myMap[num] += 1
        # print(myMap)

        # Create maxHeap comparing the frequency 
        # The maxHeap elements are tuples --> (Frequency, key)
        maxHeap = []
        for key, freq in myMap.items():
            t = (-freq, key)
            heapq.heappush(maxHeap, t)
        print(maxHeap)
        
        ans = []
        while k > 0:
            key = heapq.heappop(maxHeap)[1]
            ans.append(key)
            k -= 1
        return ans
