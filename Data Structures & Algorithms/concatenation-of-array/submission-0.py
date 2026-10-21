class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        """ 
        GOAL: we need to create a new list twice the length of nums.
            ans[i] == nums[i] AND ans[i + n] == nums[i]

        IDEA:
            - For i in range(2n)
            - At each time, we are going to set ans[i] = nums[i % n]

            e.g. nums = [1, 4, 1, 2], then we iterate 8 times
                - ans[0] = nums[0 % 4] --> 1
                - ans[4] = nums[4 % 4] --> 1
        """
        n = len(nums)
        ans = [0 for i in range(2*n)] # placeholder to hold 2n values first that we must overwrite 
        for i in range(2*n):
            ans[i] = nums[i % n]
        return ans