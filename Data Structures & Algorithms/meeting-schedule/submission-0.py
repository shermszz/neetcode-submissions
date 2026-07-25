"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        # For this question, the approach is to sort each of the intervals in the list by their END timings
        # This is a greedy approach. 

        intervals.sort(key=lambda x: x.end)
        last_end_time = 0

        # If the start_time is more than the last_end_time, then we can keep going
        for interval in intervals:
            if interval.start >= last_end_time:
                last_end_time = interval.end
            else:
                return False
        return True