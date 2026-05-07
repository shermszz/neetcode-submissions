class Solution:
    def maxArea(self, heights: List[int]) -> int:
        max_water = 0
        i, j = 0, len(heights) - 1
        while i < j:
            lower, dist = min(heights[i], heights[j]), j - i
            print("Lower is", lower)
            print("distance is", dist)
            max_water = max(max_water, lower * dist)
            print("max now is", max_water)
            print()
            if heights[i] < heights[j]:
                # we should move i forward for a chance to get higher height
                i += 1
            else:
                j -= 1
        return max_water