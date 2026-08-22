class Solution {
    public int singleNumber(int[] nums) {
        // Just run XOR in this array, since every number appears twice, which means XOR will cancel it out to become 0
        // Only the lonely number will be the result at the end
        int result = 0;
        for (int n : nums) result ^= n;
        return result;
    }
}
