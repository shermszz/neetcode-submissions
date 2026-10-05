/**
 * Definition of Interval:
 * public class Interval {
 *     public int start, end;
 *     public Interval(int start, int end) {
 *         this.start = start;
 *         this.end = end;
 *     }
 * }
 */

class Solution {
    public int minMeetingRooms(List<Interval> intervals) {
        /* 
            GOAL: Find minimum number of rooms to fit all the meetings together
            it is an overlap if the ending time of the earlier meeting ended later than the current meeting start time (i.e. prev.end > .start)
            
            First, we sort the timings in ascending order by start time

            We should maintain a minHeap to keep track of what the earliest ending time is for all meetings.
                - The minHeap should keep track of just the end times of the meetings we add into it.
                - This way, when we want to add a new meeting, we check whether its start time is less than the earliest end time.
                - If less than, that means the current meeting overlaps, and we will need to add a new room, which is to add this interval into the minHeap

                - If not less than the minimum ending time, that means we can pop the minimum then add this new interval in

            At the end, we return the length of the minHeap as the minimum number of rooms required
        */
        if (intervals.isEmpty()) return 0;
        Collections.sort(intervals, (a, b) -> a.start - b.start); 
        PriorityQueue<Integer> minHeap = new PriorityQueue<>();

        minHeap.offer(intervals.get(0).end);

        for (int i = 1; i < intervals.size(); i++) {
            Interval curr = intervals.get(i);

            if (curr.start < minHeap.peek()) {
                // That means the current meeting we need to start is overlapping with an existing one
                minHeap.offer(curr.end);
            } else {
                // This means that the current meeting we are adding does not interfere with a meeting that is ending, so we can reuse that room 
                minHeap.poll();
                minHeap.offer(curr.end);
            }
        }
        return minHeap.size();
    }
}
