class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix, pre = [], 1
        suffix, suff = [], 1
        ans = []
        prefix.append(1);
        suffix.append(1);
        for i in range(1, len(nums)):
            pre *= nums[i - 1]
            prefix.append(pre)
        # print(prefix)

        reversed_nums = nums[::-1]
        # print(reversed_nums)
        for i in range(1, len(nums)):
            suff *= reversed_nums[i - 1]
            suffix.append(suff)
        suffix.reverse()
        # print(suffix)

        for i in range(len(nums)):
            ans.append(prefix[i] * suffix[i])
        return ans;