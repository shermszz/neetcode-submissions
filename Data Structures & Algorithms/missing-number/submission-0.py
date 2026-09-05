class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)
        # The range is from [0, n]
        
        # We first do a XOR operation over every number from 0 to n
        res = 0
        for i in range(n + 1):
            res ^= i
        
        # Then, we XOR with the actual numbers in nums, which will eventually reveal the missing number at the end
        for num in nums:
            res ^= num
        
        return res