class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        # Merge all the overlapping intervals to get a final list of non overlapping intervals

        intervals.sort() # Sort the intervals by start time first
        res = [] # Final results list

        res.append(intervals[0]) # First interval gets attached first

        for i in range(1, len(intervals)):
            curr = intervals[i]
            if res[-1][1] >= curr[0]:
                # They overlap, so we need to combine the current end time with the latest res end time
                res[-1][1] = max(res[-1][1], curr[1])
            else:
                # no overlap, just append
                res.append(curr)
        return res