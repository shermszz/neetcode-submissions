class Node:
    def __init__(self, key: int, value: int):
        self.prev = None
        self.next = None
        self.key = key
        self.value = value

class LRUCache:

    def __init__(self, capacity: int):
        self.cache = {} # This is a hashmap of key value to the Node ref that contains the value
        self.dummy_head = Node(-1, -1)
        self.dummy_tail = Node(-1, -1)
        self.dummy_head.next = self.dummy_tail
        self.dummy_tail.prev = self.dummy_head
        self.capacity = capacity
        self.curr_length = 0

    def add_to_head(self, new_node: Node) -> None:
        """ Adds a new node to the linked list and the cache """
        after = self.dummy_head.next
        new_node.prev = self.dummy_head
        after.prev = new_node
        new_node.next = after
        self.dummy_head.next = new_node
        self.curr_length += 1

    def shift_to_head(self, node: Node) -> None:
        """ Shifts the `node` to the head of the linked list, and managing the pointers before and after this node"""
        previous = node.prev
        after = node.next
        node.prev, node.next = None, None
        previous.next = after
        after.prev = previous
        self.dummy_head.next.prev = node
        node.next = self.dummy_head.next
        self.dummy_head.next = node
        node.prev = self.dummy_head
    
    def remove_from_tail(self) -> None:
        """ remove the least recently used at the tail. Also remove from the cache"""
        node_to_remove = self.dummy_tail.prev
        node_to_remove.next = None
        node_to_remove.prev.next = self.dummy_tail
        self.dummy_tail.prev = node_to_remove.prev
        node_to_remove.prev = None
        
        del self.cache[node_to_remove.key]
        self.curr_length -= 1

    def get(self, key: int) -> int:
        """ Retrieve the key-based value from the cache if it exists, and then update its recent use by shifting it to the head"""
        if self.cache.get(key) is None:
            return -1
        # Update the linked list state first before returning
        # Find this item in the linked list, and then shift its pointers to the front
        self.shift_to_head(self.cache[key])
        return self.cache[key].value

    def put(self, key: int, value: int) -> None:
        """ Add a new value to the cache if there is space, otherwise we need to remove the value at the tail first, then we add 
        We could also be UPDATING the current value inside the cache, in which case we need to shift the node to the front"""
        if self.cache.get(key) is not None:
            # we wnat to perform an update
            self.cache[key].value = value
            self.shift_to_head(self.cache[key])
        else:
            # Key does not exist, so we are trying to add it into the cache
            if self.curr_length == self.capacity:
                # We are trying to add when the cache is full, so we need to remove the node at the tail, and also update the cache that it is gone
                self.remove_from_tail()
            new_node = Node(key, value)
            self.cache[key] = new_node
            self.add_to_head(new_node)


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)