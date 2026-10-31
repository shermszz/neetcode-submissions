class Node:
    def __init__(self, key: int, value: int):
        self.key = key
        self.value = value
        self.counter = 1 # Initialize a counter for this node (to monitor frequency)
        self.prev = None
        self.after = None
    
class DoublyLinkedList:
    def __init__(self):
        self.dummy_head = Node(-1, -1)
        self.dummy_tail = Node(-1, -1)
        self.dummy_head.after = self.dummy_tail
        self.dummy_tail.prev = self.dummy_head
        self.length = 0

    def remove(self, node: Node) -> None:
        # You need the 2 neighbours before this node and after this node
        prev_node, next_node = node.prev, node.after
        prev_node.after = next_node
        next_node.prev = prev_node
        node.after, node.prev = None, None
        self.length -= 1

    def addToFront(self, node: Node) -> None:
        # You need to add this to the front of the node to make it the most recently used
        # Need to attach this "node" in front of the dummy 
        current_first = self.dummy_head.after # This was the first node, now it will be the 2nd
        node.prev, node.after = self.dummy_head, current_first
        current_first.prev = node
        self.dummy_head.after = node
        self.length += 1

    def popTail(self) -> Node:
        if self.length > 0:
            node_to_pop = self.dummy_tail.prev
            self.remove(node_to_pop)
            return node_to_pop
        return None

class LFUCache:
    '''GOAL: get(key) and put(key, value) must be O(1)
        When we want to evict a node, we need to remove the one that is least frequently used 
        LFU means we need a counter for each node, if it is used the least, we remove it. 
        However, if there are multiple nodes that have the same least count value, then we need to remove the least recently used ==> Which is the LRU cache. 


    '''
    def __init__(self, capacity: int):
        # We need a few structures to keep track of certain things here
        # 1. When we call get, it needs to be reading from a Hashmap to return the Node object immediately 
        self.node_map = {} # To hold {key : Node object with its value and counter}

        # 2. We need some structure to determine the frequencies of each node and what nodes hold that count
        self.freq_map = defaultdict(DoublyLinkedList) # To hold {count : linked list of nodes with said count}. The linked list is arranged from most recently used to least recently used.
        self.lfu_count = 0 # Track the current minimum globally
        self.capacity = capacity
        self.max_capacity = capacity

    def get(self, key: int) -> int:
        # This will increment the count of the node's counter
        if key not in self.node_map:
            return -1
        
        curr_node = self.node_map[key]
    
        # We need to update the frequency map and remove this curr_node from the old linked list and add it into the new count's linked list
        prev_count = curr_node.counter
        curr_node.counter += 1
        self.freq_map[prev_count].remove(curr_node)
        
        # only increment the lfu_count if the previous count we just emptied was indeed the minimum frequency 
        if self.freq_map[prev_count].length == 0 and prev_count == self.lfu_count:
            self.lfu_count += 1

        self.freq_map[prev_count + 1].addToFront(curr_node) # add to the front of this new linked list for this new frequency 

        return curr_node.value
        

    def put(self, key: int, value: int) -> None:
        if self.max_capacity == 0:
            return
        # There are 2 scenarios: Update OR insert new node

        # 1. Say we are inserting a new node:
        if self.get(key) == -1:
            # Here, we need to check capacity
            if self.capacity == 0:
                # No more space, we need to evict something first before we insert
                # We want to immediately know what is the lowest frequency element, so we access the lowest frequency using lfu_count, and the pop the tail 
                node_to_remove = self.freq_map[self.lfu_count].popTail()
                del self.node_map[node_to_remove.key] # Also remove from the node_map
                self.capacity += 1
            # Now we actually insert of the node
            node_to_insert = Node(key, value)
            self.freq_map[node_to_insert.counter].addToFront(node_to_insert)
            self.node_map[key] = node_to_insert
            self.lfu_count = 1
            self.capacity -= 1
        # 2. If we are here, we are updating an existing node
        else:
            to_update_node = self.node_map[key]
            to_update_node.value = value # Update happens here
            # Done, no need to adjust nodes since get() already adjusted it for us



# Your LFUCache object will be instantiated and called as such:
# obj = LFUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)