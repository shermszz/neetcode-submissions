class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # prerequisites is a directed EDGE list b --> a
        # There cannot be any cycles inside this edge list when we build up the graph

        # Create an adjacency list from this edge list, then run dfs to check if there is a node we will visit more than once. 
        # Need to use the 3 colour idea

        adj_list = defaultdict(list)
        for course, prereq in prerequisites:
            adj_list[prereq].append(course) # prereq is the key --> course to take after prereq
        
        visited = [0 for i in range(numCourses)] # Initialize a list of 0's to represent unvisited
        # If a course is partially visited, label with a 1
        # Once the course has been fully visited, we change its cell to 2

        def dfs(course_num):
            if visited[course_num] == 1:
                # If earlier calls already returned false OR we encountered a cycle
                return False
            
            if visited[course_num] == 2:
                # ignore
                return True
            
            visited[course_num] = 1
            list_of_future_courses = adj_list[course_num] # list_of_future_courses of the given course_num
            # Complete them first by running dfs on them
            for course in list_of_future_courses:
                if not dfs(course): # If any of the below future courses have a cycle, we return False here
                    return False
            
            # Once done, mark this course as completed.
            # No other courses should depend on this now
            visited[course_num] = 2
            return True

        for i in range(numCourses):
            if not dfs(i): # If any of the dfs calls are false, we short circuit out and return False
                return False
        return True

"""
=========================================================
KEY LEARNINGS: Course Schedule (LeetCode 207)
=========================================================

CORE CONCEPTS:
1. The Adjacency List: The most efficient way to represent a directed 
   graph. Build it using a Hash Map or Array of Lists: 
   `adj_list[source].append(destination)`.
2. 3-State DFS Cycle Detection: Standard 2-state visited sets create 
   "False Cycles" on cross-edges (when two valid paths merge). 
   You MUST use 3 states:
   - State 0 (Unvisited): Never seen before.
   - State 1 (Visiting): Currently in the recursive call stack. 
     (If you step on a 1, you found a true cycle!)
   - State 2 (Fully Visited): Completely explored and proven safe. 
     (If you step on a 2, safely ignore it).
3. The "Bubble Up" Pattern: Pure recursive functions must listen to 
   their children. Use `if not dfs(neighbor): return False` to instantly 
   propagate a failure up the entire call stack.

GUIDING HINTS & TRAPS AVOIDED:
- The Disconnected Graph Trap: Not all courses are connected. You 
  MUST wrap your initial DFS launch in a `for` loop from 0 to 
  `numCourses - 1` to ensure you check isolated islands/components!
- The Overwrite Trap: Never do `res = dfs(i)` in a loop. It overwrites 
  previous failures. Always short-circuit with early returns.
=========================================================
"""