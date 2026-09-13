class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        """
        Split into 3 phases:
        1. Go through all the initial intervals first. 
            while the newInterval start time is > the interval end time we are looking at, we just add the current interval into a result list

        2.  Once the first phase breaks, we will need to perform a merge between the new interval and the current interval that we stopped. When we merge, we need to continouslty check to make sure rest of the intervals are not overlapping. Otherwise, we continously merge and update the [start, end] to add, shifting index appropriately

        3. Then, in this last phase, we will just attach the remaining intervals while index < len(intervals) 
        """
        index = 0
        n = len(intervals)
        res = []
        # Phase 1
        while index < n and intervals[index][1] < newInterval[0]:
            res.append(intervals[index])
            index += 1
        
        # Phase 2: Where newInterval finally overlaps with the current interval pointed to by index. Keep resolving the overlaps until we no longer overlap
        while index < n and intervals[index][0] <= newInterval[1]:
            # We specificaly check for the current Start <= new interval END because the new interval can be merged and spread further to the left. We need to see if the current event would have started while we are still new Interval ended. 
            newInterval[0] = min(newInterval[0], intervals[index][0])
            newInterval[1] = max(newInterval[1], intervals[index][1])
            index += 1
        res.append(newInterval)

        # Phase 3: Clean up any remaining intervals if any
        while index < n:
            res.append(intervals[index])
            index += 1
        
        return res


