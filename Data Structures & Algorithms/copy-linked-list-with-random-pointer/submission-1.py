"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""
from collections import OrderedDict
class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        # Edge case: If list empty, return empty list
        if not head:
            return head
        # First pass, iterate through the old list, copying all the nodes into a hashmap
        myMap = {}
        old_node = head
        while old_node:
            new_node = Node(old_node.val, None, None) # Leave the next and random pointers empty first
            myMap[old_node] = new_node # Key = old_node, Value = new_node
            old_node = old_node.next

        # Second pass, iterate through the old list again, but now with reference to the hashmap
        curr = head
        while curr:
            new_node = myMap[curr]
            new_node.next = myMap.get(curr.next) # use .get() to ensure we do not get KeyError for missing keys, in case pointers point to NULL
            new_node.random = myMap.get(curr.random)
            curr = curr.next
        
        return myMap[head]
