class Solution:
    def jump(self, nums: List[int]) -> int:
        jumps = 0
        left, right = 0, 0
        
        while right < len(nums) - 1: 
            # while the right boundary is not at the end of the array yet
            # We need to continue to track what is the next "window" by checking how far we can jump from the value that we are currently at right now
            farthest_index = 0
            for i in range(left, right + 1):
                farthest_index = max(farthest_index, i + nums[i])
            
            left = right + 1
            # Once we have the farthest index that we can jump to, we set that as right boundary
            right = farthest_index
            jumps += 1
        return jumps

