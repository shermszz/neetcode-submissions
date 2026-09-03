class Solution:
    def canJump(self, nums: List[int]) -> bool:
        n = len(nums)
        # Each value in nums is the MAX value that we can jump. 
        # So what we do is to track at each position, if we jump any amount from 0 to val, can we each the end successfully?
        # We can run a dfs algorithm with memoization to track each position in the list whether it is possible or not during overlapping work

        memo = {} # to store index in the array : can we reach the end boolean

        def dfs(index: int) -> bool:
            if index in memo: # Dont repeat the work again
                return memo[index]
            if index == n - 1:
                # If we successfully reached the end of the array, then we can return True
                return True
            if index >= n:
                return False
            jump_val = nums[index]
            if jump_val == 0:
                # There is nowhere to go to anymore, and we are not at the end, so we failed
                return False
            # Otherwise, for each jump_value from 1 to jump_val, we want to track each value from 1 to jump_val and see whether any of these values allows us to reach the end
            res = False
            for i in range(1, jump_val + 1):
                res = res or dfs(index + i)
            memo[index] = res
            return res

        memo[0] = dfs(0)
        return memo[0]
