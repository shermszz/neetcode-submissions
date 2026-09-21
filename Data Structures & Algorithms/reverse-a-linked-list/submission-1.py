# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head
        
        # We will just traverse the head and keep changing its next pointer to point to the previous one
        prev = None
        after = head.next

        while after:
            head.next = prev
            prev = head
            head = after
            after = after.next
        head.next = prev
        return head
        
        