class Solution {
    public int longestConsecutive(int[] nums) {
        if (nums.length == 0) return 0;
        HashSet<Integer> set = new HashSet<>();
        for (int num : nums) set.add(num);

        int longest = 1;
        for (int num : set) {
            if (set.contains(num - 1)) continue; // There is a longer sequence
            int count = 1; int curr = num;
            while (set.contains(curr + 1)) {
                count++; curr++;
            }
            longest = Math.max(count, longest);
        }
        return longest;
    }
}
