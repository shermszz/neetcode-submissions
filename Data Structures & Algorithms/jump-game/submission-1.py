class Solution:
    def canJump(self, nums: List[int]) -> bool:
        # This is solvable via Greedy solution
        # We want to check from the last position, is it possible to make it to the start of the array
        n = len(nums)
        goal = n - 1

        for i in range(n - 2, -1, -1):
            curr_jump_val = nums[i]
            if i + curr_jump_val >= goal:
                goal = i # Shift the goal down to this position, since it is possible to reach the end from position i
        return goal == 0