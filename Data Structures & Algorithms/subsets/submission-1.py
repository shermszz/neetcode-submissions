class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res, n = [], len(nums)

        def backtrack(index, current_bucket):
            # 1. Base case: If there are no more numbers to process, we save this current_bucket as a COPY
            if index >= n:
                res.append(current_bucket.copy())
                return
            curr_num = nums[index]

            # 2. INCLUDE new number
            current_bucket.append(curr_num)
            backtrack(index + 1, current_bucket) # Recurse with this new number

            # 3. EXCLUDE the same number we just added
            current_bucket.pop()
            backtrack(index + 1, current_bucket) # Recurse without this new number

        backtrack(0, [])
        return res

"""
=========================================================
KEY LEARNINGS: Subsets (LeetCode 78)
=========================================================

CORE CONCEPTS:
1. Backtracking vs. DP: Backtracking is an exhaustive search. 
   It explores every possible path in a decision tree. Dynamic 
   Programming is about saving answers to avoid repeated work. 
2. The "Yes/No" Decision Tree: Generating subsets means asking 
   one question for every element: "Do I include this, or exclude it?"
3. The Backtracking Rhythm (The Single Bucket):
   - MAKE CHOICE: Put the item in the bucket (`append`).
   - EXPLORE: Move to the next item (`backtrack(index + 1)`).
   - UNDO CHOICE: Take the item out (`pop`).
   - EXPLORE: Move to the next item without it (`backtrack(index + 1)`).

GUIDING HINTS:
- The Base Case: You hit the end of a path when your index equals 
  the length of the array (`index == n`). 
- The Python Copy Trap: When saving a list to your final results, 
  you MUST append a copy (`res.append(bucket.copy())` or `bucket[:]`). 
  Otherwise, your future `pop()` calls will empty the saved answers!
- Fast Removal: Use `.pop()` instead of `.remove()` to instantly chop 
  off the last item in O(1) time without scanning the array.
=========================================================
"""