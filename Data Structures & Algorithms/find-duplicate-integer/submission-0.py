class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        slow, fast = 0, 0
        # First, we need to find where slow and fast pointers collide
        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]
            if slow == fast: break
        # Once we have found where they collided, we reset slow to the start, and let fast keep looping in the cycle
        slow = 0
        while slow != fast:
            slow = nums[slow]
            fast = nums[fast]
        return slow

"""
=========================================================
KEY LEARNINGS: Find the Duplicate Number (LeetCode 287)
=========================================================

CORE CONCEPTS:
1. Array as a Linked List: When array values are strictly bounded 
   within the size of the array (values in range [1, n]), you can 
   treat the values as 'next' pointers. (e.g., nums[0] = 3 means 
   jump from index 0 to index 3).
2. Floyd's Cycle Detection (Tortoise & Hare): The optimal O(1) space 
   and O(n) time algorithm for finding cycles. Because there is a 
   duplicate number, multiple indices will point to the same target 
   index, mathematically guaranteeing a cycle.

GUIDING HINTS:
- The Trap: A HashSet works but is O(n) space. Sorting modifies the array.
- Phase 1 (Find the Crash Site): 
    - Slow pointer takes 1 step: `slow = nums[slow]`
    - Fast pointer takes 2 steps: `fast = nums[nums[fast]]`
    - Loop until they collide (`slow == fast`).
- Phase 2 (Find the Duplicate/Entrance): 
    - Leave `fast` at the crash site. 
    - Reset `slow` back to the starting line (`0`). 
    - Move BOTH pointers exactly 1 step at a time. 
    - The exact node where they collide again is your duplicate!
=========================================================
"""
        