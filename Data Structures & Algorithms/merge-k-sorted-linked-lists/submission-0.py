# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        # Since there are k Linked Lists, we need to merge them in sorted order 
        # We should use a min heap to store each linked list node
        minheap = [] # heap in python is default MIN heap
        for index, node in enumerate(lists):
            if node:
                heapq.heappush(minheap, (node.val, index, node)) # Takes in the head of the other linked lists
        # Once all the heads are collected inside the minheap, start to pop from the minheap into a new sorted list
        dummy = ListNode(0, None)
        curr = dummy
        while minheap:
            val, index, nextSmallest = heapq.heappop(minheap)
            if nextSmallest.next:
                heapq.heappush(minheap, (nextSmallest.next.val, index, nextSmallest.next))
            curr.next = nextSmallest
            curr = curr.next
        return dummy.next

"""
=========================================================
KEY LEARNINGS: Merge k Sorted Lists (LeetCode 23)
=========================================================

CORE CONCEPTS:
1. K-Way Merge: When combining multiple sorted lists, a Min-Heap 
   is the optimal structure. It constantly bubbles up the absolute 
   minimum of the "current" nodes in O(log k) time.
2. Time/Space Complexity: 
   - Time: O(N log k), where N is total nodes, k is number of lists.
   - Space: O(k) for the heap, as it only holds 1 node per list at a time.

GUIDING HINTS:
- The Python Tuple Trick (Simulating a Comparator):
  Python's `heapq` lacks a custom comparator and compares tuples 
  element-by-element (left-to-right). 
  * If you push `(node.val, node)`, it crashes on duplicate values 
    because it tries to compare `node < node`.
  * The Fix: Push `(node.val, list_index, node)`. By injecting a 
    unique integer (the index) in the middle, Python resolves ties 
    using the index and NEVER attempts to compare the actual nodes!

- The Conveyor Belt: Don't just pop from the heap! Every time you 
  pop `node`, you must immediately check `if node.next:`. If it exists, 
  push `node.next` into the heap using the SAME `list_index` to keep 
  that list's conveyor belt moving.

- Edge Case Trap: The input array might contain empty linked lists 
  (e.g., `[[], [1,2]]`). Always check `if node:` before doing the 
  initial push into the heap.
=========================================================
"""



