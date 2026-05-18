class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums) - 1
        while left <= right:
            mid = left + ((right - left) // 2)
            print("nums[mid] is", nums[mid])
            # now, we check whether target is larger, smaller or equal to mid to determine where to shift our pointers
            if nums[mid] == target:
                return mid
            if nums[left] <= nums[mid]:
                # This means the left half is perfectly sorted
                # Hence, we can check here in this perfectly sorted array whether target lies in this region
                if nums[left] <= target and target <= nums[mid]:
                    right = mid - 1
                else:
                    # This means it is on the other side
                    left = mid + 1
            else:
                # This means the right half is perfectly sorted
                if nums[mid] <= target and target <= nums[right]:
                    left = mid + 1
                else:
                    right = mid - 1
        return -1
