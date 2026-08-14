class Solution {
    public int search(int[] nums, int target) {
        int l = 0;
        int r = nums.length - 1;

        while (l <= r) {
            int mid = l + ((r - l) / 2);
            int curr = nums[mid];
            if (curr == target) {
                return mid;
            } else if (curr < target) {
                // The actual number lies on the RHS
                l = mid + 1;
            } else{
                // The actual number lies on the LHS
                r = mid - 1;
            }
        }

        //If still cannot find, then it doesnt exist
        return - 1;
    }
}
