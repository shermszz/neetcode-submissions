class Solution {
    public int search(int[] nums, int target) {
        // Finding the target sum inside the array to see if it exists or not
        int left = 0; int right = nums.length - 1;
        while (left <= right) {
            int mid = left + (right - left) / 2;
            System.out.println("Checking index " + mid + " now with value " + nums[mid]);
            // When splitting the array in half, we know that one side of the array is properly sorted while the other might be out of order
            if (nums[mid] == target) {
                return mid;
            }

            // Otherwise, we need to look left or right for the target
            // But since it is not sorted, only 1 side is guaranteed sorted
            // Hence, we first need to find which is the sorted array. 
            // Once we know which side is sorted, we check if target actually fits anywhere between that range. If so, we search the sorted region, otherwise we search the unsorted one
            
            if (nums[mid] < nums[right]) {
                // This means that the array RHS is sorted
                if (target <= nums[right] && target > nums[mid]) {
                    // If target is in range of this sorted portion, we search here
                    left = mid + 1;
                } else {
                    // Otherwise, we throw it to search the other unsorted portion
                    right = mid - 1;
                }
            } else {
                // This means the array LHS is sorted
                if (target < nums[mid] && target >= nums[left]) {
                    right = mid - 1;
                } else {
                    left = mid + 1;
                }
            }
        }
        return -1;
    }
}
