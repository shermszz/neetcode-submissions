class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        """ 
        we want a subarray whose sum == k
        that means sum(i, j) == k
        sum(i, j) = prefix[j + 1] - prefix[i]
        [2, -1, 1, 2]
        prefix = [0, 2, 1, 2, 4]
        if i want the subarray(0, 1) --> that would be prefix[2] - prefix[0] = 1 - 0 = 1
        we want prefix[j + 1] - k = prefix[i]
        Therefore, we need to maintain a hashmap {prefix sum : how many times it appeared}
        We need this because we want to check how many times the difference in prefix[j + 1] - k appears.
            Because this will tell us exactly how many prefixes before when we remove it, will actually form the sum k that we want

        """
        prefix = [0]
        count_map = defaultdict(int)
        count_map[0] = 1 # This is a trivial case thing, cuz if we have a prefix sum array whose sum == k itself, hence prefix[j + 1] - k == 0, we can remove the "empty" subarray at the start

        running_sum = 0
        num_subarrays = 0
        for i in range(len(nums)):
            running_sum += nums[i]
            prefix.append(running_sum)
            if (prefix[i + 1] - k) in count_map:
                num_subarrays += count_map[prefix[i + 1] - k]
            count_map[running_sum] += 1
        return num_subarrays


