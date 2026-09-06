class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        """ 
        Case 1:
            (1, 3) (1, 5) and (6, 7)
            merge the overlapping regions. 
            (1, 5), (6, 7)

        Case 2: 
            (6, 7), (2, 6), (1, 4)
            sort gets (1, 4), (2, 6), (6, 7)
            Loop from index 1 up till the end, checking the current start and prev_end
            If the current start (2) <= previous end (4): (true)
                We need to merge here
                output --> (1, 6)
                current start = minimum of the 2 start intervals
                end is gna be the maximum of the 2 end intervals
                append to the result array
            Otherwise if (false):
                We dont need to merge, just append the the current interval into the result array
        
        """

        # 1. sort the array by the start date. 
        intervals.sort(key=lambda x: x[0])
        
        res = []
        # Grab the first interval from the intervals list
        res.append(intervals[0])

        for i in range(1, len(intervals)):
            curr_start, curr_end = intervals[i][0], intervals[i][1]
            # Checking if curr_start <= prev_end
            # To get the previous end, we can just peek at the result array tail
            if curr_start <= res[-1][1]:
                res[-1][0] = min(curr_start, res[-1][0])
                res[-1][1] = max(curr_end, res[-1][1])
            else:
                # There is no overlap, so we just merge the current interval in
                res.append(intervals[i])
        return res



