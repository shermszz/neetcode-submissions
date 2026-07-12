class Solution:
    def foreignDictionary(self, words: List[str]) -> str:
        # words is sorted lexographically
        # There are 2 conditions for 2 strings to be lexographically smaller:
            # 1a. At least one letter must be different in the 2 strings
            # OR
            # 1b. a.length < b.length

        # Use a 2 pointer approach.
        # Iterate through words one by one, comparing their prefixes first, and then comparing their length
        # We can build up a directed graph to find the order of letters later using topological sort

        def find_first_difference(word1: str, word2: str) -> tuple | None: 
            """Finds the first letter difference between the 2 words"""
            # 1. Case when word1.length <= word2.length
            i = 0
            found = False
            while i < len(word1) and i < len(word2):
                if word1[i] != word2[i]:
                    found = True
                    break
                i += 1

            if not found and len(word1) > len(word2):
                # This is an invalid scenario, we immediately signal to return the empty string
                return None
            # Otherwise, if we have yet to find a difference, then we have no information about the order of characters
            if not found:
                return () # Return an empty tuple to indicate to move on
            else:
                word1_char, word2_char = word1[i], word2[i]
                return (word1_char, word2_char) # word1_char < word2_char lexographically. 

        adj_list = defaultdict(set)
        in_degree = {} # To store the in_degrees of each letter that appears in words
        for word in words:
            for i in range(len(word)):
                # for each unique character, set their in-degree to be 0 first
                if word[i] not in in_degree:
                    in_degree[word[i]] = 0
        
        for i in range(len(words) - 1):
            first, second = words[i], words[i + 1]
            res = find_first_difference(first, second)
            if res is None:
                return ""
            if res == ():
                continue
            char1, char2 = res # Where char1 < char2
            if char2 not in adj_list[char1]:
                adj_list[char1].add(char2)
                in_degree[char2] += 1
        
        print("adj_list", adj_list)
        print("in_degree", in_degree)
        # Once we have our adj_list set up, and in_degree set up, we can begin Kahn's algorithm
        # We first find those with in_degree == 0, and then run BFS and add them to a result list
        queue = deque()
        result = [] # To store the lexographical ordering, return as a string later on using .join
        for letter, degree in in_degree.items():
            if degree == 0:
                queue.append(letter)
        
        while queue:
            curr = queue.popleft()
            result.append(curr)
            for neighbour in adj_list[curr]:
                in_degree[neighbour] -= 1
                if in_degree[neighbour] == 0:
                    queue.append(neighbour)
        print("result is", result)
        if len(result) != len(in_degree):
            # This means that there couldve been a cycle in the dictionary, so if the length of result doesnt match up, we return the empty string
            return ""
        return "".join(result)

"""
=========================================================
KEY LEARNINGS: Alien Dictionary (LeetCode 269 / 114)
=========================================================

CORE CONCEPTS:
1. Extracting Order from Strings: Comparing sorted words only gives you 
   information about the FIRST differing character. E.g., "wrt" vs "wrf" 
   means `t` comes before `f`. The remaining letters tell you nothing.
2. Topological Sort (Kahn's Algorithm): Whenever a problem asks you to 
   find a valid linear sequence based on "prerequisites" or "orderings", 
   build a directed graph and use Kahn's Algorithm (In-Degree counting).
3. The Three Graph Components:
   - Adjacency List: Maps a node to all its outgoing connections.
   - In-Degree Map: Counts how many incoming arrows point to a node.
   - Zero-Degree Queue: A queue that holds nodes with 0 incoming arrows 
     (meaning all their prerequisites are met and they are ready to process).

GUIDING HINTS & TRAPS AVOIDED:
- The Invisible Letter Trap: Always initialize the `in_degree` map with 
  EVERY unique item before building edges. Otherwise, items with no rules 
  will completely vanish from your final result.
- The Prefix Trap: In a valid dictionary, a longer word can NEVER come 
  before its own prefix (e.g., "apple" before "app" is illegal).
- The Cycle Detector: If your final sorted array is shorter than the 
  total number of unique nodes, the graph contains a cycle (a paradox 
  where A -> B -> A), making a linear order impossible.
=========================================================
"""
            
            
