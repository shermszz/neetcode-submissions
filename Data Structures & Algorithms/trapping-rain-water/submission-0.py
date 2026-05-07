class Solution:
    def trap(self, height: List[int]) -> int:
        #Naive solution first:
        max_water = 0
        n = len(height)
        # For every index, find the tallest wall to the left, and tallest wall to the right
        for i in range(n):
            # Find the max wall to the left of i
            max_left = 0
            for j in range(i + 1):
                max_left = max(height[j], max_left)
            max_right = 0
            for j in range(i, n):
                max_right = max(height[j], max_right)

            water_level = min(max_left, max_right)
            max_water += (water_level - height[i])
        return max_water
            
            