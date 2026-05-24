# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        first = head
        while n > 0:
            first = first.next
            n -= 1
        second = head
        prev = None
        while first:
            first = first.next
            second = second.next
            if prev == None:
                prev = head
            else: 
                prev = prev.next
        # Now, second is on the node we want to remove
        if second == head:
            return head.next
        after = second.next
        second.next = None
        prev.next = after
        return head



