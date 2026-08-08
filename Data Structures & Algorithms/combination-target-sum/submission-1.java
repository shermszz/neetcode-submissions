class Solution {

    private void backtrack(List<List<Integer>> result, HashSet<List<Integer>> set, int[] nums, List<Integer> bucket, int index, int runningSum, int target) {
        //Base case: when index at the end of the array or the running sum exceeded the target
        if (index == nums.length || runningSum > target) {
            return;
        }
        if (runningSum == target) {
            // Then we save the array inside result
            // Check if the bucket is already in a set that contains the bucket we are about to add
            if (!set.contains(bucket)) {
                set.add(bucket);
                result.add(new ArrayList<>(bucket));
            }
            return;
        }

        // Otherwise, we still need to continue to fill the bucket up
        /*
            Scenario 1: We can choose the number, but we do not move the index forward, because we can take unlimited of the say number if we want
            Scenario 2: We choose the number, and move the index forward
            Scenario 3: We dont choose the number, we move the index forward
        */
        int currNum = nums[index];
        
        // Scenario 1
        bucket.add(currNum);
        runningSum += currNum;
        backtrack(result, set, nums, bucket, index, runningSum, target);

        //Scenario 2
        backtrack(result, set, nums, bucket, index + 1, runningSum, target);

        //Scenario 3
        bucket.remove(bucket.size() - 1);
        runningSum -= currNum;
        backtrack(result, set, nums, bucket, index + 1, runningSum, target);

    }
    public List<List<Integer>> combinationSum(int[] nums, int target) {
        // The idea is that for nums, we can either take or not take a value. 
        // Base case is if the value combined is more than the target, we discard
            // If value combined == target, we save it into the output array
        List<List<Integer>> result = new ArrayList<>();
        HashSet<List<Integer>> set = new HashSet<>();
        List<Integer> bucket = new ArrayList<>();
        backtrack(result, set, nums, bucket, 0, 0, target);

        return result;
    }
}
