class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # Since we must take course b first, that means we must take b before a
        # Hence, the edge should point from b --> a
        adj_list = defaultdict(list)
        in_degree = [0 for _ in range(numCourses)]
        for v, u in prerequisites:
            adj_list[u].append(v) # We must take u first before taking v
            in_degree[v] += 1
        
        # We can use BFS to determine whether it is possible to finish all courses 
        # We will have a queue, initialized with all the courses that do not require any prerequisites (i.e. in-degree of zero)
        queue = deque()
        courses_visited = 0
        for i in range(numCourses):
            if in_degree[i] == 0:
                queue.append(i) # The courses that have no prerequisities start here
            
        # Then, we will iterate through the queue, everytime we consume a neighbour, we reduce their in-degree and if zero, we add them to the queue. 
        # We can keep track of the courses that we have completed
        while queue:
            curr_course = queue.popleft()
            courses_visited += 1
            for neighbour in adj_list[curr_course]:
                in_degree[neighbour] -= 1
                if in_degree[neighbour] == 0:
                    queue.append(neighbour)

        return courses_visited == numCourses




