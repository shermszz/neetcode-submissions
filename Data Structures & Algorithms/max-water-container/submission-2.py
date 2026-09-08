class Solution:
    def maxArea(self, heights: List[int]) -> int:
        """
        The plan here is to have 2 pointers, one at the start, and another at the end. 
        Then, we will calculate the full area within it, but the sides are bounded to the minimum of the 2 (i.e. water_volume = length * min(start, end))
        Then, we just have a running maximum to keep track of it

        To decide which pointer to move in, we will always move the pointer whose next value has a higher bar. If there is a drop, then we will shift the pointer with a smaller drop so that we can maximise the water 
        """
        max_water = -1
        start, end = 0, len(heights) - 1

        while start < end:
            length = end - start
            curr_water = length * min(heights[start], heights[end])
            max_water = max(max_water, curr_water)

            if heights[start] < heights[end]:
                # If the left bar is shorter than the right bar now, we want to maximise the water, so we shift the left bar forward
                start += 1
            else:
                end -= 1
        return max_water
