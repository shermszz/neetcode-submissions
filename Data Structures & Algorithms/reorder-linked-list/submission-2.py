# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        # For this question the trick is to find the mid point of the list, reverse the 2nd half of the list, and then merge the 2 lists together to form the new reordered linked list
        if not head or not head.next:
            return

        # 1. Use fast and slow pointers to get the mid point of the list
        fast, slow = head, head
        while fast.next and fast.next.next:
            fast = fast.next.next
            slow = slow.next
        
        # Now, slow pointer will be pointing at the end of the first list
        second_half = slow.next
        slow.next = None # Detach it
        
        # 2. Reverse the list from the slow pointer onwards
        prev, curr = None, second_half.next
        while second_half:
            second_half.next = prev
            prev = second_half
            second_half = curr
            if curr:
                curr = curr.next
        # Now, prev is the new head position of the reversed list

        # 3. Now, we merge the two lists together
        l1, l2 = head, prev
        dummy = ListNode()
        curr = dummy
        while l1 and l2:
            # Attach to the first list
            curr.next = l1
            curr = curr.next
            l1 = l1.next

            # Attach to the 2nd list
            curr.next = l2
            curr = curr.next
            l2 = l2.next
        if l1:
            # In case of odd numbered linked lists, attach the last node from l1, since l1 will have 1 more node to add
            curr.next = l1