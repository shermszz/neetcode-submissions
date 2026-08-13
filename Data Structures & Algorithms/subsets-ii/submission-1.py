class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        # First, we sort the array so that duplicates will be next to each other
        nums.sort()
        # print(nums)
        result = []

        # This is the same backtracking idea, we either include and continue, or exclude and stop
        def backtrack(bucket: list[int], index: int) -> None:
            # 1. Base case
            if index == len(nums):
                result.append(bucket.copy())
                return
            
            # 2. Now, we first choose to include the number
            bucket.append(nums[index])
            backtrack(bucket, index + 1)

            # 3. Next, we exclude the number and try again
            # However, if we want to exclude this number, we need to exclude all duplicates of this number
            while index < len(nums) - 1 and nums[index] == nums[index + 1]:
                index += 1
            
            bucket.pop()
            backtrack(bucket, index + 1)

        backtrack([], 0)
        return result