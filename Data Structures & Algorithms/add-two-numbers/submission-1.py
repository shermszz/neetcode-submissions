# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(0, None)
        curr = dummy
        carry = 0
        while l1 or l2 or carry: # need to have an "or carry" condition, in case a carry over occurs while both lists are done
            n1 = l1.val if l1 else 0
            n2 = l2.val if l2 else 0
            total = n1 + n2 + carry
            carry = total // 10 # either 1 or 0
            digit = total % 10 # extract the digit out 
            node = ListNode(digit, None)
            curr.next = node
            curr = curr.next
            l1 = l1.next if l1 else l1
            l2 = l2.next if l2 else l2
        return dummy.next
