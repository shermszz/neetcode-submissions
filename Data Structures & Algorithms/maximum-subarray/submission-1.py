class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        # maintain a dp array where each position tells us what the maximum sum is at that point
        n = len(nums)
        curr_sum = nums[0]
        max_sum = nums[0]
        
        for i in range(1, n):
            # the could either take the current value or not
            # If i take the value, I will add it to my current maximum
            # Otherwise, if i dont take the value, i will start again at the current value I am at
            curr_sum = max(nums[i], curr_sum + nums[i])
            max_sum = max(curr_sum, max_sum)
        
        return max_sum
