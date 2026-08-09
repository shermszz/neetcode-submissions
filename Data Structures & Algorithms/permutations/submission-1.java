class Solution {

    private void backtrack(List<List<Integer>> result, List<Integer> bucket, int[] nums, boolean[] used) {
        if (bucket.size() == nums.length) {
            result.add(new ArrayList<>(bucket));
            return;
        } 

        for (int i = 0; i < nums.length; i++) {
            if (used[i]) continue; // The number has taken this slot

            used[i] = true;
            bucket.add(nums[i]);
            backtrack(result, bucket, nums, used);

            used[i] = false;
            bucket.remove(bucket.size() - 1);
        }
    }

    public List<List<Integer>> permute(int[] nums) {
        List<List<Integer>> result = new ArrayList<>();
        List<Integer> bucket = new ArrayList<>();
        boolean[] used = new boolean[nums.length];
        Arrays.fill(used, false);
        backtrack(result, bucket, nums, used);

        return result;
    }
}
