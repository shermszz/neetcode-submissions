class Solution {
    public int findMin(int[] nums) {
        int left = 0;
        int right = nums.length - 1;
        
        while (left < right) {
            int mid = left + (right - left) / 2;
            // In a rotated sorted array, only one half of the array can be possibly out of order
            // 1. the right side is out of order
            if (nums[mid] > nums[right]) {
                // This means the array fell on the right side, which means that smallest element lies on the right side of the array for sure
                left = mid + 1;
            } else {
                // if nums[mid] <= nums[right], this means the minimum element lies on the left OR is on mid itself
                right = mid;
            }

        }
        // Both pointers will eventually converge 
        return nums[left];

    }
}
