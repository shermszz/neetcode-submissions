class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        """
        A naive approach would be to be for each i, for each j, check each k --> O(n^3)
        One thing we can do is first sort the array in non-descrighting order
        e.g. nums = [-4, -1, -1, 0, 1, 2]
        Then, from this sorted array, we have a fixed pointer for every value in the array
            For each value, we generate 2 pointers and calculate whether the total sum is equal to 0 or not --> O(n^2) time
            We do not wnat duplicates, so we need to ensure that as we go along, we do not reuse the same values in the outer loop and in the inner loop
        """

        nums.sort()
        res = []
        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i - 1]: # Checking for duplicate values in outer loop
                continue
            left, right = i + 1, len(nums) - 1
            while left < right:
                # using 2 pointer logic, we try to find the sum
                curr_sum = nums[i] + nums[left] + nums[right]
                if curr_sum == 0:
                    ans = [nums[i], nums[left], nums[right]]
                    res.append(ans)
                    left += 1
                    right -= 1
                    while left < right and nums[left] == nums[left - 1]: # Prevent duplciates in the inner loop
                        left += 1
                elif curr_sum < 0:
                    # value is too small, we need a larger one
                    left += 1
                else:
                    # value bigger than 0, make it smaller
                    right -= 1
        return res 