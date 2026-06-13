class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res, n = [], len(nums)

        def backtrack(index, current_bucket):
            # 1. Base case: If there are no more numbers to process, we save this current_bucket as a COPY
            if index >= n:
                res.append(current_bucket.copy())
                return
            curr_num = nums[index]

            # 2. INCLUDE new number
            current_bucket.append(curr_num)
            backtrack(index + 1, current_bucket) # Recurse with this new number

            # 3. EXCLUDE the same number we just added
            current_bucket.pop()
            backtrack(index + 1, current_bucket) # Recurse without this new number

        backtrack(0, [])
        return res
