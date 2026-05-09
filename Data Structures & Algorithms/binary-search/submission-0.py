class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1
        while l <= r:
            mid = l + ((r - l) // 2)
            # print("Middle is", mid)
            if nums[mid] == target:
                return mid
            elif nums[mid] > target:
                # Value must be on the left
                r = mid - 1
            else:
                # Value must be on the right
                l = mid + 1
        # If the value does not exist
        return -1
            