class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        # Use a Doubly Linked List
        self.next = None 
        self.prev = None

class LRUCache:

    def __init__(self, capacity: int):
        self.cache = {} # This hashmap needs to be of size = capacity only
        self.left = Node(-1, -1) # The "dummy head" of the DLL
        self.right = Node(-1, -1) # The "dummy tail" of the DLL
        self.capacity = capacity

        # Connect the two dummy nodes together first
        self.left.next = self.right
        self.right.prev = self.left
    
    def shiftToTail(self, node):
        left, right = node.prev, node.next
        left.next, right.prev = right, left
        node.prev, node.next = None, None

        # After detaching, now attach this node to the tail end
        leftTail = self.right.prev
        self.right.prev = node
        node.next = self.right
        node.prev = leftTail
        leftTail.next = node
    
    def remove(self, node):
        left, right = node.prev, node.next
        left.next, right.prev = right, left
        node.prev, node.next = None, None

        # Capacity increases by 1 
        self.capacity += 1
        del self.cache[node.key]

    def add(self, node):
        # This is for new nodes, add them to the linked list
        # By default, will always add to the Tail end, since once we add, it is most recently used
        leftTail = self.right.prev
        self.right.prev = node
        node.prev = leftTail
        node.next = self.right
        leftTail.next = node

        # Capacity now drops by 1
        self.capacity -= 1
        self.cache[node.key] = node # add into the hashmap the key --> node reference

    def get(self, key: int) -> int:
        # Return the value, but also shift this node to the tail of the linked list
        nodeToGet = self.cache.get(key)
        if not nodeToGet: # If the node to get does not exist
            return -1
        # Update the linked list to shift this node to the back to be the most recently used
        self.shiftToTail(nodeToGet)
        return nodeToGet.value


    def put(self, key: int, value: int) -> None:
        node = self.cache.get(key)
        # First, check if the node exists
        if node: # If key exists, update the value
            node.value = value
            self.shiftToTail(node)
        else:
            # Now, check if there is space in the cache to put this new node
            if self.capacity <= 0:
                self.remove(self.left.next)
                self.put(key, value) # Attempt to put again.
            else:
                # Create a new node to add into the cache
                newNode = Node(key, value)
                self.add(newNode)
"""
=========================================================
KEY LEARNINGS: LRU Cache (LeetCode 146)
=========================================================

CORE CONCEPTS:
1. The Holy Grail Combo: O(1) lookups require a Hash Map. 
   O(1) shifting/evictions require a Doubly Linked List.
2. The Two Bookends: Always use TWO dummy nodes (`left` and `right`). 
   Sandwiching all real nodes between two immovable bookends 
   completely eliminates "Empty List" NoneType edge cases.

GUIDING HINTS:
- Structure your Node: `key`, `value`, `prev`, `next`. (You MUST 
  store the key in the node so you know what to delete from the 
  Hash Map when the node gets evicted!).
- Build 2 clean Helpers: `remove(node)` and `add(node)`. Do not 
  mix capacity tracking into these pointer-math helpers.
- Hash Map Syncing: Every time you physically add a node to the 
  DLL, you MUST add it to the Hash Map. Every time you remove 
  from the DLL, you MUST `del` it from the Hash Map.
- To update a node's recency: `remove(node)` -> `add(node)`. 
  Don't write a 3rd function for shifting!
=========================================================
"""
