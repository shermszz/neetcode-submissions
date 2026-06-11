import random
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        
        target_index = len(nums) - k

        def quick_select(start, end):
            # Utilize randomization for average O(N) solution
            random_pivot_index = random.randint(start, end)
            nums[start], nums[random_pivot_index] = nums[random_pivot_index], nums[start]

            pivot = nums[start]
            p = start

            for i in range(start + 1, end + 1):
                if nums[i] <= pivot:
                    p += 1
                    nums[p], nums[i] = nums[i], nums[p]
            
            # Move pivot into its correct position
            nums[p], nums[start] = nums[start], nums[p]

            if p == target_index:
                return nums[p]
            elif p < target_index:
                return quick_select(p + 1, end)
            else:
                return quick_select(start, p - 1)
        
        return quick_select(0, len(nums) - 1)
        
"""
=========================================================
KEY LEARNINGS: Kth Largest Element in an Array (LeetCode 215)
=========================================================

CORE CONCEPTS:
1. The Elimination Heap (Your Code): Heapify the whole array O(N), 
   then pop N-k times. Best when k is close to N.
2. The VIP Club Heap: Maintain a Min Heap of size k. Push/Pop 
   for every element. Best when k is very small. Time: O(N log k).
3. Quickselect (The True Optimal): Use a pivot to partition the 
   array. Discard half the array each iteration. 
   Average Time: O(N). Worst Case Time: O(N^2) if you pick bad pivots.

GUIDING HINTS:
- For LeetCode, the Heap solutions are perfectly acceptable and 
  often preferred for their reliable performance. 
- Quickselect is the "gold standard" for this specific problem 
  in an interview setting to demonstrate mastery of array partitioning.
=========================================================
"""

