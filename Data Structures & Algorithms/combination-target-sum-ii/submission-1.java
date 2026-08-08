class Solution {

    private void backtrack(List<List<Integer>> result, int[] nums, List<Integer> bucket, int index, int runningSum, int target) {
        // If the running Sum is equal to the target, we have found one solution
        if (runningSum == target) {
            result.add(new ArrayList<>(bucket));
            return;
        }

        //Base case: if index has exceeded its boundaries or the runningSUm has already exceeded the target value
        if (index == nums.length || runningSum > target) return;

        // Otherwise, we need to continue to monitor the number of items to add
        // 1. We can choose to include this number and then move on
        bucket.add(nums[index]);
        runningSum += nums[index];
        backtrack(result, nums, bucket, index + 1, runningSum, target);

        // 2. We can exclude this number, and try other combinations
        // but this time, if we choose to exclude, we need to make sure all of the same numbers are actually excluded, which is why we sort them at the start
        bucket.remove(bucket.size() - 1);
        runningSum -= nums[index];
        while (index + 1 < nums.length && nums[index] == nums[index + 1]) {
            index++;
        }
        backtrack(result, nums, bucket, index + 1, runningSum, target);

    }

    public List<List<Integer>> combinationSum2(int[] candidates, int target) {
        List<List<Integer>> result = new ArrayList<>();
        List<Integer> bucket = new ArrayList<>();
        Arrays.sort(candidates); // We need to sort so that we can keep track of duplicate numbers
        // System.out.println(Arrays.toString(candidates));

        backtrack(result, candidates, bucket, 0, 0, target);
        return result;
    }
}