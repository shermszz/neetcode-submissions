class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        """
           Goal: Count the min number of intervals to remove such that every interval does not overlap any other interval
           The overlapping condition is when ending of the interval is smaller than the start of another interval 
           QUESTION: Can there be duplicated interval values inside intervals? --> I assume yes
           Steps:
            1. Sort the array by starting time first so that we can compare each interval side by side

            e.g.: intervals = [[1, 2], [2, 4], [1, 4]]
            After sorting ==> [[1, 2], [1, 4], [2, 4]]
            From here, we iterate through the sorted intervals list and maintain a count of number of overlapping intervals that we see
            We check for each interval, is the ending of curr interval > start of the next interval
                [1, 2] and [1, 4] ==> 2 > 1 is false (hence, there is an overlap we need to resolve)

            Now the question is, which interval to remove?
                - if I remove [1, 2], then im left with [1, 4] and the next check will be [2, 4], which overlaps again. Then i would need to remove the interval again in the next run
                - if i remove [1, 4] instead, I will get a better minimum answer. 

            From here, lets try choosing what to remove to be the interval that has a larger range, because there would be a higher chance that this larger range interval overlaps with other intervals. If they have the same range, we remove the interval with a larger end value point (THIS IS WRONG)

            (CORRECT VERSION) We should remove the range that ended later regardless of the range

        """
        intervals.sort(key=lambda x:x[0])
        # print(intervals)
        count = 0 # To track how many intervals we are removing
        previous_end = intervals[0][1]

        for i in range(1, len(intervals)):
            if previous_end > intervals[i][0]:
                # print("Overlap detected at index", i)
                # This means there is an overlap between the interval in res and current interval
                # We need to resolve which interval to remove
                curr_end = intervals[i][1]
                if previous_end > curr_end:
                    # we remove the previous interval, so we need to update the previous_end value now
                    previous_end = curr_end
                # else, we would remove the curr interval, which we do by simply ignoring it
                count += 1
            else:
                # Since there is no overlap, we can simply add the interval into the res list
                previous_end = intervals[i][1]
            # print(res)

        return count




