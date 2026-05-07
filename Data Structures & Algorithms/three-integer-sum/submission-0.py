class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # Sort nums in non-decreasing order first
        sorted_nums = sorted(nums)
        ans = []
        for i in range(len(sorted_nums)):
            if i > 0 and sorted_nums[i - 1] == sorted_nums[i]:
                continue
            j, k = i + 1, len(sorted_nums) - 1
            while j < k:
                # Compare the triplet values, if we find a triplet == 0, put it in a list and append to ans
                sum = sorted_nums[i] + sorted_nums[j] + sorted_nums[k]
                if sum < 0:
                    # Too small, increase j pointer
                    j += 1
                elif sum > 0:
                    # Too big, decrease k pointer
                    k -= 1
                else:
                    # Found a triplet
                    triplet = [sorted_nums[i], sorted_nums[j], sorted_nums[k]]
                    ans.append(triplet)
                    j += 1
                    k -= 1
                    while j < k and sorted_nums[j - 1] == sorted_nums[j]:
                        j += 1
                    while k > j and sorted_nums[k + 1] == sorted_nums[k]:
                        k -= 1
        return ans