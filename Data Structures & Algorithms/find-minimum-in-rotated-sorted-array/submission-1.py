class Solution:
    def findMin(self, nums: List[int]) -> int:
        left, right = 0, len(nums) - 1
        # The right side should be bigger than the left
        # In case where right < left, then we should shift left to the right
        # If left < right, then we should shift right to the left
        while left < right:
            mid = left + ((right - left) // 2)
            if nums[mid] < nums[right]:
                # A smaller value exists on the left side or at mid itself
                right = mid # Do not -1 here, because the minimum could be mid itself.
            elif nums[mid] > nums[right]:
                # That means a smaller value is on the right
                # So we shift left to mid + 1
                left = mid + 1
            else:
                # Guranteed unique elements, should never reach here
                print("should never reach here")
        return nums[left] 
        # OR return nums[right] no diff