class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        longest = 0
        left = 0
        # We need a dictionary of all unique characters and their earliest index positions
        my_map = {}

        for right in range(len(s)):
            curr_char = s[right]
            
            # 1. Update left pointer only if the curr_char is inside the map and if the duplicate is in the window
            if curr_char in my_map and my_map[curr_char] >= left:
                left = my_map[curr_char] + 1
            
            # 2. Always record the freshest index
            my_map[curr_char] = right
            
            # print("my_map is", my_map)
            # print("left =", left, "and right =", right)
            longest = max(longest, right - left + 1)
        return longest


"""
s = xyxabcd
output should be 6 => "yxabcd"

"""



       