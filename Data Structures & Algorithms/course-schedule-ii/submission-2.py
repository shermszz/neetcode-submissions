class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        # return a topological order
        topo_sort_arr = []
        adj_list = defaultdict(list)
        in_degrees = [0 for _ in range(numCourses)]
        for v, u in prerequisites:
            adj_list[u].append(v)
            in_degrees[v] += 1
        
        queue = deque()
        # Initialise a queue with all the courses with indegree = 0 
        for i in range(numCourses):
            if in_degrees[i] == 0:
                queue.append(i)
        while queue:
            curr_course = queue.popleft()
            topo_sort_arr.append(curr_course)
            for neighbour in adj_list[curr_course]:
                in_degrees[neighbour] -= 1
                if in_degrees[neighbour] == 0:
                    queue.append(neighbour)
        return topo_sort_arr if len(topo_sort_arr) == numCourses else []