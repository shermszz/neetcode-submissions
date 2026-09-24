"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        """
           GOAL: Find the minimum number of rooms such that all room schedules have no conflicts.
           Conflict is defined by the starting of the next interval overlapping with the ending of the previous interval
            - i.e. if start_i+1 < end_i, then there is a conflict and we need to have separate rooms. 

            First, lets sort by end time : (WRONG) (WE MUST SORT BY START TIME SINCE SCHEDULING)
                sorted intervals = [(5, 10), (15, 20), (0, 40)]
            We are going to have default 1 room first, which we will place the first interval into.
            Then, for the rest, we need to check if there is a conflict with ALL the rooms.
                - Only then we need to create a new room.
                - To check for conflicts within the rooms, we need to iterate across all rooms, and we can use a hashmap since order doesnt matter.
                - Hashmap will store room_number:latest end time
            If there is a room where there is no conflict, we can place this interval inside this room.

            Otherwise if we conflict with every room, we need to create a new room, and then add this interval inside 

            What do need to keep track for each room?
                - We need to track what is the latest end time per room, so that when we encounter a new interval, we know where to place them based on the end times of each room.
                
        
            CORRECT VERSION:
            We need to use a min heap data structure to store the earliest ending times for each meeting after sorting by START time
            Then, wheever we want to add a new interval, we check what is the earliest time any of the meetings would end, so we just need to read the minHeap at the top minHeap[0]
            If that value itself conflicts with our incoming start time, we know we need to have a new room for sure. We also need to add the incoming end time into the heap
            Otherwise, if no conflict, we can simply use that room, and then just pop the old timing and add the new one in.
            At the end, we know how many rooms we need by simply checking the length of the min_heap, because each value inside represents the number of distinct rooms we need to have in order to not conflict 
        """
        # Edge case, if intervals is empty
        if not intervals:
            return 0
        
        intervals.sort(key = lambda x:x.start) # Sort by the end times
        min_heap = []
        heapq.heappush(min_heap, intervals[0].end) # Push the first interval into the minHeap

        # Now, lets iterate over the rest of the intervals
        for i in range(1, len(intervals)):
            # First, lets check if there is a conflict with the meeting that ends the earliest
            if intervals[i].start >= min_heap[0]:
                # There is no conflict, we pop this value and add this new one in
                heapq.heappop(min_heap)
                heapq.heappush(min_heap, intervals[i].end)
            else:
                # There is a conflict with every room since we cannot start when the earliest one has finished, so we need to add a new room
                heapq.heappush(min_heap, intervals[i].end)
        return len(min_heap)
            

         