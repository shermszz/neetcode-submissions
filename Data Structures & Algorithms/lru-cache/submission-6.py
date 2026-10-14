class LRUCache:
    class Node:
        def __init__(self, key: int, value: int):
            self.key = key
            self.value = value
            # Doubly linked list pointers in a node
            self.prev = None
            self.after = None 
        
    def __init__(self, capacity: int):
        # We probably need a hashmap somewhere in order to retrieve the values quickly.
        # We need a doubly linked list in order to adjust the and quickly shift Nodes to the front if they were recently used or to the back
        self.node_map = {} # used to store the key --> retrieve the Node itself
        self.capacity = capacity
        
        # Create the first 2 initial nodes and connect them together first
        self.dummy_prev = self.Node(0, 0) 
        self.dummy_after = self.Node(0, 0)
        self.dummy_prev.after = self.dummy_after
        self.dummy_after.prev = self.dummy_prev

    def get(self, key: int) -> int:
        # Must run in O(1) --> We would need a hashmap in order to find the value quickly
        if key not in self.node_map:
            return -1
        node = self.node_map[key]
        self.remove_node(node)
        self.add_to_front(node)
        return node.value

    def remove_node(self, node: Node) -> None:
        # We remove the current node and reattach its neighbours together
        previous = node.prev
        after_node = node.after
        previous.after = after_node
        after_node.prev = previous
        node.prev = None 
        node.after = None

    def add_to_front(self, node: Node) -> None:
        # We add this node to the front of the linked list
        after_node = self.dummy_prev.after
        self.dummy_prev.after = node
        node.prev = self.dummy_prev
        node.after = after_node
        after_node.prev = node


    def put(self, key: int, value: int) -> None:
        # Must run in O(1)
        # We want to either UPDATE or ADD a new key-value pair
        if self.get(key) == -1:
            # This is an Addition
            # We need to check whether there is enough space to add this new node or not
            if self.capacity == 0:
                # We need to remove the least recently used, which is the node at the back
                to_remove = self.dummy_after.prev
                self.remove_node(to_remove)
                del self.node_map[to_remove.key]
                self.capacity += 1 # Now we have 1 more free slot
            
            new_node = self.Node(key, value)
            self.node_map[new_node.key] = new_node # Add this node into the hashmap
            self.add_to_front(new_node)
            self.capacity -= 1
        else:
            # This is an UPDATE
            curr = self.node_map[key]
            curr.value = value # Update the value
    
