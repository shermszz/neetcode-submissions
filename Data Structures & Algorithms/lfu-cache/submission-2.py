class DoublyLinkedList:
    def __init__(self):
        self.dummy_head = Node(-1, -1)
        self.dummy_tail = Node(-1, -1)
        self.dummy_head.next = self.dummy_tail
        self.dummy_tail.prev = self.dummy_head
        self.length = 0

    def add_to_front(self, node):
        # Given this node, add the node to the front of the linked list
        # This is for the LRU order
        second_node = self.dummy_head.next
        self.dummy_head.next = node
        node.next = second_node
        second_node.prev = node
        node.prev = self.dummy_head
        self.length += 1
    
    def remove_node(self, node):
        # Detach the current node from its neighbours
        behind, front = node.prev, node.next
        behind.next = front
        front.prev = behind
        node.prev = None
        node.next = None
        self.length -= 1
    
    def pop_tail(self):
        # Removing the least recently used node
        node_to_remove = self.dummy_tail.prev
        self.remove_node(node_to_remove)
        return node_to_remove.key


class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.prev = None
        self.next = None
        self.count = 1

class LFUCache:
    """ 
        To implement LFU, the idea is to have a 2 Hash maps and for each frequency count, we have a doubly linked list
        For example: (frequency map)
        {
            1: O <--> O <--> O ....
            2: O <--> O <--> O ....
            3: O <--> O
            4: O <--> O <--> O ....
            5: 
            ...
        }
        Within each doubly linked list, it needs to be in LRU order so that in case of clashes with the LFU, we can still remove the least recently used one in O(1), which will be at the tail.

        We still need a node_map to map the key --> Node directly

    """

    def __init__(self, capacity: int):
        self.cap = capacity
        self.max_capacity = capacity # read only
        self.node_map = {}
        self.freq_map = defaultdict(DoublyLinkedList)
        self.lfu_count = 1 # The least frequently used global count so that we know what row in the hashmap to remove values from.

    def get(self, key: int) -> int:
        # When we call get, we just need to check if the key currently exists in the node_map
        if key not in self.node_map:
            return -1
        
        curr_node = self.node_map[key]
        # We need to update its count and its recency value
        prev_count = curr_node.count # Old count that we need to remove 
        curr_node.count += 1

        self.freq_map[prev_count].remove_node(curr_node)
        self.freq_map[prev_count + 1].add_to_front(curr_node)

        if self.freq_map[prev_count].length == 0 and prev_count == self.lfu_count:
            self.lfu_count += 1

        return curr_node.value

    def put(self, key: int, value: int) -> None:
        if self.max_capacity == 0:
            return 
        # There are 2 cases for a put. Either we are inserting a new value OR we are updating a new value
        if self.get(key) == -1:
            # 1. Inserting a new value, but now we need to check if we need to evict any values or not
            if self.cap == 0:
                # Time to evict the least frequently used value
                old_key = self.freq_map[self.lfu_count].pop_tail()
                del self.node_map[old_key]
                self.cap += 1
            
            new_node = Node(key, value)
            self.lfu_count = 1 # Because we have a new value we need to reset the count to 1
            self.freq_map[self.lfu_count].add_to_front(new_node)
            self.node_map[key] = new_node
            self.cap -= 1
        else:
            # 2. Updating an existing value
            # the get() method already increments the count for us, so we don't have to do it twice
            to_update_node = self.node_map[key]
            to_update_node.value = value # Update the value


# Your LFUCache object will be instantiated and called as such:
# obj = LFUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)


