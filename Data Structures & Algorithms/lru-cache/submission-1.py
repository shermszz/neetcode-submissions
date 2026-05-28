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

