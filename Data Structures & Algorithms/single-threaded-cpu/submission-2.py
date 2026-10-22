class Solution:
    def getOrder(self, tasks: List[List[int]]) -> List[int]:
        """
        GOAL: Return the order in which the CPU will be executing each task 

        Tasks will come in at enqueueTime and will take processingTime to execute

        Since we need the order in which they are executed, we need to first sort by the enqueueTime from earliest to latest. The secondary sorting criteria would be the processing time

        Example: tasks = [[5,2],[4,4],[4,1],[2,1],[3,3]]

        1. We first sort by enqueueTime then Processing time:
        But we need their index information so we can first create a tuple containing (enqueue time, processing time, index)
            sorted tasks = [(1, 2, 3), (3, 3, 4), (1, 4, 2), (4, 4, 1), (2, 5, 0)]

        Once we have these tasks sorted, we will always enqueue the first task and we record its index
        res = [3]
        cpu_time = 1

        We need to keep track of the current time as well as how long the CPU is currently still being used
        Track in a for loop, as time increases, cpu_time decreases, and we need to dynamically know what is the next task to execute the moment we hit a cpu_time of 0
        We also need to track with some data structure the jobs that are waiting. 
        For jobs that are waiting, we need to dynamically know which ones have the lowest processing time and then we execute those --> use a MIN_HEAP for this 
        If cpu_time > 0, that means we are still processing so we do not schedule anything. 
        If cpu_time == 0, CPU is idle and if there are pending jobs, we will add them to the cpu_time
        In every iteration, we need to track the time for the next few jobs to enter
        """
        cpu_time = 0
        n = len(tasks) # Number of tasks 
        res = [] # To hold the indices of the tasks that will be executed in order
        tasks_with_index = []
        for index, (enq, proc) in enumerate(tasks):
            tasks_with_index.append((proc, enq, index))
        
        tasks_with_index.sort(key=lambda x: x[1]) # This will sort by enqueueTime
        q = deque(tasks_with_index)
        min_heap = [] # To store the shortest task at the top

        curr_time = q[0][1] if q else 0
        while q or min_heap: # if there are still tasks to be assigned OR if there are still tasks that are waiting to be run on the CPU
            # 1. If CPU is idle and no tasks are queued, fast forward to the next earliest task
            if not min_heap and q[0][1] > curr_time:
                curr_time = q[0][1]

            while q and q[0][1] <= curr_time:
                proc_time, _, index = q.popleft()
                heapq.heappush(min_heap, (proc_time, index))

            # Check for any available task that is waiting
            processing_time, index = heapq.heappop(min_heap)
            # print("Allocated task", index, "with time =", processing_time)
            res.append(index) # We are now processing this task
            # print("result now is", res)
            curr_time += processing_time # Fast forward the time
        return res







