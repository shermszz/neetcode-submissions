class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        freq = Counter(tasks) # To find the number of times each task needs to be executed
        print(freq)
        waiting_queue = deque() # To store the next time we should allow a task to come back to ready_queue
        max_heap = [-c for c in freq.values()]
        heapq.heapify(max_heap)
        print(max_heap)
        
        time = 0
        while max_heap or waiting_queue:
            # 1. Check the queue FIRST
            if waiting_queue and waiting_queue[0][1] == time:
                # This means this task will be ready
                val, t = waiting_queue.popleft()
                heapq.heappush(max_heap, -val)
            
            time += 1 
            
            # 2. Now process the heap / ready_queue
            if max_heap:
                top = -1 * heapq.heappop(max_heap)
                if top > 1:
                    pair = (top - 1, time + n)
                    waiting_queue.append(pair)
        return time
"""
=========================================================
KEY LEARNINGS: Task Scheduler (LeetCode 621)
=========================================================

CORE CONCEPTS:
1. Greedy Scheduling: Always schedule the most frequent available 
   task first. If you don't, you'll be left with high-frequency tasks 
   and nothing to put between them, forcing massive idle times.
2. The "Waiting Room" Pattern: 
   - Max Heap: Holds tasks currently ready to execute.
   - Queue: Holds tasks on cooldown. Stores tuples of `(count, ready_time)`.

GUIDING HINTS:
- Loop Order Matters: Always check the Waiting Room (Queue) to see 
  if anyone is ready to return to the Heap BEFORE you pull from the Heap. 
- Fast-Forwarding Time: If the Heap is empty, don't simulate every 
  single idle second. Fast-forward `time` directly to the `ready_time` 
  of the first task in the Queue.
=========================================================
"""

