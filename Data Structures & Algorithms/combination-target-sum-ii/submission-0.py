class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort() # Sort candidates first for the exclude step later
        res, n = [], len(candidates)

        def backtrack(curr_index: int, curr_sum: int, bucket: List[int]) -> None:
            if curr_index == n or curr_sum >= target:
                if curr_sum == target:
                    res.append(bucket.copy())
                return
            next_num = candidates[curr_index]
            bucket.append(next_num)
            # can only choose the number at most once, so we move forward the index regardless
            backtrack(curr_index + 1, curr_sum + next_num, bucket)

            # In this exclude step, we need to exclude all duplicates of the same number
            # FAST-FORWARD: Skip all identical copies of the number we just rejected!
            num_to_skip = bucket.pop()
            while curr_index < n and candidates[curr_index] == num_to_skip:
                curr_index += 1
            backtrack(curr_index, curr_sum, bucket)
        
        backtrack(0, 0, [])
        return res

"""
=========================================================
KEY LEARNINGS: Combination Sum II (LeetCode 40)
=========================================================

CORE CONCEPTS:
1. The "Parallel Universe" Trap: When your input array has 
   duplicates (e.g., two `1`s), including the first `1` and excluding 
   the second creates the EXACT same mathematical subset as excluding 
   the first and including the second.
2. Group the Clones: You MUST sort the array before backtracking 
   so identical numbers are adjacent. This turns duplicates into a 
   single block you can easily skip.
3. The Fast-Forward Exclude: If you say "No" to a number, you must 
   say "No" to ALL identical copies of it. Use a `while` loop during 
   the "Exclude" step to push the index past the duplicates.

GUIDING HINTS & TRAPS AVOIDED:
- Python Sorting Trap: `sorted(arr)` returns a NEW list and leaves 
  the original untouched. Always use `arr.sort()` to sort in-place!
- Pruning: Sorting takes O(N log N), but by skipping duplicate branches, 
  you save the computer from exploring O(2^N) useless paths. In 
  backtracking, sorting is the ultimate optimization.
=========================================================
"""
