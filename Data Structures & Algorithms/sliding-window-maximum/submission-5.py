class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        # We want to slide the window across each position to track what the largest element is inside the window at this point.
        # One thing to maintain is a deque. 
        # deque[0] always contains the index of the maximum in the window we are in
        # Everytime there is a bigger value about to enter, we keep removing right from the deque because this bigger value will outlast everything else that is older, so no point tracking them
        # If the value about to enter is smaller, we just append to the right
        # If the index falls out of the range, we must remember to remove it from the deque
        dq = deque()
        res = []
        index = 0
        curr_max = -float('inf')
        while index < len(nums):
            # 1. Check if the number we are about to add is bigger than what is inside the deque now
            while dq and nums[dq[-1]] <= nums[index]:
                dq.pop()
            
            dq.append(index) # Append the index of the current number

            # 2. Now check whether the number on the left most is still valid or not
            if dq[0] < index - k + 1:
                dq.popleft() # Invalid index now should not consider

            # After all that, we know that the deque first entry contains the maximum in the window that we are in right now
            # We should only append to our result once the window is fully built
            if index >= k - 1:
                res.append(nums[dq[0]])
            index += 1
        return res
