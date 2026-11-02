# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        """ 
            GOAL: remove the nth node from the end of the list

            If the length of the list is L, then removing the nth node means we should move n times from the left first, then travel until the we hit the end and then have the first pointer pointing to the node we want to remove

            E.g. = [1, 2, 3, 4], L = 4, n = 4 remove the 4th node from the end is val 1.
            We initialize a left pointer and then move left n = 4 times to the right --> left points to 4

            Then, initialize a curr pointer at the head, and then move forward as long as the left pointer is not at the end (i.e. not null).
            Since left is already at the end of th list, the node to remove is the value 1 that is pointed to by curr. 

            2nd e.g. = [1, 2, 3, 4, 5], L = 5, n = 2 ==> Remove 4
            left = head, move it 2 times. points to 3
            curr = head.
            move let two times, move curr two times and lands at 3

        """
        left = head
        for i in range(n):
            left = left.next
        
        curr = head
        dummy = ListNode()
        dummy.next = curr
        prev = dummy
        while left is not None:
            curr = curr.next
            prev = prev.next
            left = left.next

        # curr now points to the node that we need to remove it with the prev and after pointer
        after = curr.next
        prev.next = after
        curr.next = None
        return dummy.next
