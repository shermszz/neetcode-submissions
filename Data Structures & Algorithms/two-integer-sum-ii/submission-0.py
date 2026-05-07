class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        # Input array is already sorted, so we just use 2 pointer approach
        left, right = 0, len(numbers) - 1
        while left < right:
            curr = numbers[left] + numbers[right];
            if curr == target:
                # Found the indices, return it
                return [left + 1, right + 1] # Make it 1-based indexing
            elif curr > target:
                # Curr too big, need to shift right down
                print(curr, " not equal to", target, ". Too big")
                right -= 1
            else:
                # curr too small, need to shift left up
                print(curr, " not equal to", target, ". Too small")
                left += 1
        return [] # Should never reach here since answer is guranteed