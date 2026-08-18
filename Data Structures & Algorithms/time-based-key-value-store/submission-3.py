class TimeMap:
    # In this data structure, each key could be a list of values, where each value is distinguished by their timestamp

    def __init__(self):
        self.time_map = defaultdict(list) # A dictionary of lists

    def set(self, key: str, value: str, timestamp: int) -> None:
        # Setting is adding to the list of values for that particular key, which will include the timestamp
        # We can maybe use a tuple of (timestamp, value) to easily compare later to get a value
        self.time_map[key].append((timestamp, value))

    def get(self, key: str, timestamp: int) -> str:
        if not self.time_map.get(key):
            return ""
        list_of_values = self.time_map[key]
        # We need to find the value with said timestamp, this is where we can use binary search since the timestamp is always increasing
        left, right = 0, len(list_of_values) - 1
        while left <= right:
             #print("left and right are", left, right)
            mid = left + (right - left) // 2
            curr_timestamp = list_of_values[mid][0]
            # print("mid index is", mid, "and curr_timestamp is", curr_timestamp)
            if curr_timestamp == timestamp:
                # print("found a match")
                return list_of_values[mid][1]
            
            # Otherwise, check whether the current timestamp value is higher or lower
            if curr_timestamp < timestamp:
                # This means that the actual timestamp is on the RHS
                 #print("curr_timestamp < timestamp", curr_timestamp, "<", timestamp)
                left = mid + 1
                # print("left is now", left)
            else:
                # print("curr_timestamp > timestamp", curr_timestamp, ">", timestamp)
                right = mid - 1
                # print("right is now", right)
        # If we did not find it, we would be returning the next highest timestamp value just before timestamp
        if right < 0:
            return ""
        return list_of_values[right][1]
""" 

=========================================================
KEY LEARNINGS: Time Based Key-Value Store (LeetCode 981)
=========================================================

CORE CONCEPTS:
1. Appending to Sorted Arrays: If a problem guarantees that inputs arrive 
   in strictly increasing order (like a timestamp), simply appending them 
   to an array automatically creates a sorted array in $O(1)$ time. 
2. The Binary Search Pointers Post-Loop: When a standard `while left <= right` 
   binary search fails to find an exact match, the loop breaks exactly when 
   the pointers cross. 
   - The `right` pointer ALWAYS rests on the FLOOR (largest value < target).
   - The `left` pointer ALWAYS rests on the CEILING (smallest value > target).
3. The Out-of-Bounds Edge Case: Because `right` points to the floor, if 
   the target is smaller than the 0th element in the array, `right` will 
   cross over `0` and become `-1`. You MUST check `if right < 0` before 
   using it as an index to prevent crashes.

INTERVIEW LEVEL-UP (The Bisect Library):
- In a real Python interview, after explaining the binary search logic, you 
  can tell the interviewer, "In production, I would just use Python's built-in 
  `bisect` module here." 
- `idx = bisect.bisect_right(list_of_values, timestamp, key=lambda x: x[0])` 
  finds the exact insertion point in one line of C-optimized code!
=========================================================

"""