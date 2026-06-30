class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        # This version is to find the topological order
        # Build the adj_list, where for each course, it will be a list of its prerequisites. 
        # Then, we calculate the in-degree of each node to find out how many prerequisites that course has
            # This means we should have adj_list[prereq] = list of next courses
        
        # Then, loop thorugh the adj_list, find all those whose list of prerequisites is zero in length
            # These are the ones we can take immediately, hence we push them into the queue.
            # Run BFS
            # As we run BFS, we need to remove the in-degree of the course, which is to remove the course from the list of prerequisites
            # if there are no more prerequisites for that course, we can then add it into the queue 
        # Return the resultant list, but check if len(result) == numCourses, otherwise return []. 
            # If len(result) < numCourses, that means there exist a cycle 
        
        queue = deque()
        adj_list = defaultdict(list)
        in_degree_list = defaultdict(int)
        for course, prereq in prerequisites:
            adj_list[prereq].append(course) # Each prereq is a list of courses it can unlock
            in_degree_list[course] += 1 # Since it has 1 prerequsite
        
        result = []
        # Now, find those courses with 0 in degree and add them to the queue 
        for i in range(numCourses):
            if in_degree_list[i] == 0:
                queue.append(i)
        print("Initial state of queue", queue)
        # Now, we run a regular BFS
        while queue:
            course_num = queue.popleft()
            result.append(course_num) # Already in-degree 0, so we can just take it and add to our topological order

            list_of_next_courses = adj_list[course_num]
            for course in list_of_next_courses:
                # Reduce their in-degree by one
                in_degree_list[course] -= 1
                if in_degree_list[course] == 0:
                    queue.append(course) # Join the queue as a next potential course to take
        return result if len(result) == numCourses else []

"""
=========================================================
KEY LEARNINGS: Course Schedule II (LeetCode 210)
=========================================================

CORE CONCEPTS:
1. Kahn's Algorithm (BFS): The standard for Topological Sorting. 
   - Step 1: Count the `in_degree` (prerequisites) for every node.
   - Step 2: Queue up all nodes with an `in_degree` of 0.
   - Step 3: Pop a node, add it to your topological order, and 
     decrement the `in_degree` of all its neighbors. If a neighbor 
     hits 0, put it in the queue!
2. Array vs. Hash Map: If nodes are numbered strictly from `0` to `N-1`, 
   always use a flat array (e.g., `in_degree = [0] * N`) instead of a 
   Hash Map. It is faster and uses less memory.

GUIDING HINTS & TRAPS AVOIDED:
- Cycle Detection via Length: You don't need complex cycle detection 
  logic. Just compare the length of your final topological array to 
  the total number of nodes. If `len(result) < numCourses`, a cycle 
  trapped the remaining nodes!
- Forward-Facing Edges: Even though the problem gives you 
  [course, prerequisite], your adjacency list MUST point forward: 
  `adj_list[prerequisite].append(course)`. You need to know what to 
  unlock next!
=========================================================
"""