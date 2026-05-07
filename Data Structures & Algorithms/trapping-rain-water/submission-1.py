class Solution:
    def trap(self, height: List[int]) -> int:
        max_water, n = 0, len(height)
        prefix, suffix = [], []
        prev = -1
        for i in range(n):
            curr = height[i]
            if curr > prev:
                prefix.append(curr)
                prev = curr
            else:
                prefix.append(prev)
        # print(prefix)
        prev = -1
        for i in range(n - 1, -1, -1):
            curr = height[i]
            if curr > prev:
                suffix.append(curr)
                prev = curr
            else:
                suffix.append(prev)
        suffix.reverse()
        # print(suffix)

        for i in range(n):
            curr_height = height[i]
            highest_wall = min(prefix[i], suffix[i])
            water_trapped = highest_wall - curr_height
            max_water += water_trapped
        return max_water

            
            