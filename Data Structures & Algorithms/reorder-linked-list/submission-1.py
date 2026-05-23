# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        if not head or not head.next:
            # If empty list or only 1 element
            return
        fast, slow = head, head
        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next
        # List 1 is from head to the node just before slow
        # List 2 is from slow to the end
        # Now we need to reverse list 2
        prev, l2 = None, slow.next
        slow.next = None # Detach l1 from l2
        after = l2.next
        while l2:
            l2.next = prev
            prev = l2
            l2 = after
            after = after.next if after else None
        # Now prev is pointing at the last element
        # Merge the 2 together now in order
        dummy = ListNode()
        curr = dummy
        while head and prev:
            curr.next = head
            head = head.next
            curr = curr.next
            curr.next = prev
            prev = prev.next
            curr = curr.next
        if head:
            curr.next = head
        if prev:
            curr.next = prev


        


