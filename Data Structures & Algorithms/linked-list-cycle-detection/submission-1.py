# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        slow, fast = head, head
        if not head or not head.next: # If the list is empty
            return False
        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next
            if fast == slow:
                return True
        return False
    

