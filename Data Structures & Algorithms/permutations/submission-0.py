class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res, n = [], len(nums)

        def backtrack(curr_bucket: List[int]) -> None:
            # 1. Base case, the length of the bucket is already the maximum, means it contains all elements 
            if len(curr_bucket) == n:
                res.append(curr_bucket.copy())
                return
            
            # 2. Otherwise, we loop through nums to see if there is any number not already inside the bucket
            for num in nums:
                if num not in curr_bucket:
                    # Add the number if it is not inside the bucket
                    curr_bucket.append(num)
                    backtrack(curr_bucket)
                    # Once done, we remove it from the bucket
                    curr_bucket.pop()
        backtrack([])
        return res

"""
=========================================================
KEY LEARNINGS: Permutations (LeetCode 46)
=========================================================

CORE CONCEPTS:
1. The Loop Takes the Wheel: Unlike Subsets, you do not need two 
   separate recursive calls (Include vs. Exclude). The `for` loop 
   automatically handles branching by testing every available number 
   one by one.
2. The "Bouncer": Because you loop from the beginning of the array 
   every time, you MUST check if a number is already in your bucket 
   (`if num not in curr_bucket`) to avoid picking the same item twice.
3. Pop == Reset: In Permutations, `pop()` does not mean "Exclude this 
   number forever." It means "I'm done exploring the futures where 
   this number was in this specific chair. Take it out so the loop 
   can try putting the next number in this chair."

INTERVIEW LEVEL-UP (The O(1) Lookup):
- In Python, `if num not in curr_bucket` takes O(N) time because it 
  has to scan the list. Since N is very small in this problem (N <= 6), 
  it runs perfectly fine. 
- If an interviewer asks to optimize it, you can pass a `visited` Set 
  (or boolean array) alongside your bucket to make checking if a number 
  is used instant O(1) time!
=========================================================
"""