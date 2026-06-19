class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        # 1. Create a hashmap that stores { number : list of all letters }
        if not digits:
            return []
        num_to_letters = {
            '2' : ['a', 'b', 'c'],
            '3' : ['d', 'e', 'f'],
            '4' : ['g', 'h', 'i'],
            '5' : ['j', 'k', 'l'],
            '6' : ['m', 'n', 'o'],
            '7' : ['p', 'q', 'r', 's'],
            '8' : ['t', 'u', 'v'],
            '9' : ['w', 'x', 'y', 'z'],
        }
        res = []
        def backtrack(curr_index, curr_string):
            if len(curr_string) == len(digits):
                # Number of digits we have == number of letters we form for one string exactly
                res.append(curr_string)
                return
             
            curr_digit = digits[curr_index]
            associated_list = num_to_letters[curr_digit]
            for letter in associated_list:
                # 1. Include all the elements in the list associated with the curr_digit        
                backtrack(curr_index + 1, curr_string + letter)
                # Then, we want to remove it and add the next one. 
                # Since curr_string + letter generates a new string, the curr_string remains intact
        backtrack(0, "")
        return res

"""
=========================================================
KEY LEARNINGS: Letter Combinations of a Phone Number (LeetCode 17)
=========================================================

CORE CONCEPTS:
1. Implicit "Exclude" with Strings: Because strings are immutable in 
   Python, `curr_string + letter` creates a brand new string for the 
   recursive call. The parent function's `curr_string` never changes, 
   meaning you DO NOT need a second recursive call or `.pop()` to undo 
   the choice. The `for` loop handles the branching effortlessly.
2. DFS == Backtracking: When the number of nested loops you need 
   changes based on the input length (e.g., input "2" needs 1 loop, 
   input "23" needs 2 nested loops), you cannot use standard `for` loops. 
   You MUST use recursion (DFS) to dynamically travel deeper.

GUIDING HINTS & TRAPS AVOIDED:
- Type Mismatch Trap: If your input is a string (e.g., `"23"`), make 
  sure your dictionary keys are also strings (`'2'`), not integers (`2`).
- The Empty Input Edge Case: Always check if the input string is empty 
  right at the start (`if not digits: return []`). Otherwise, a string 
  backtracking template will often return `[""]` instead of `[]`.
=========================================================
"""

