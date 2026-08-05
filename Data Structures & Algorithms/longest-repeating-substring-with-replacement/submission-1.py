class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        # You want to find the string with the longest substring containing only 1 character
        # Naturally, a greedy approach is to first find the number of occurences of each character in the string, we would want to maximise the count of the character that has the highest count so far if possible
        # But we must make sure they it is contiguous as well. 

        # Maybe we can use a sliding window for this problem instead.
        # The trick is to have always check as we go, whether our current window size is valid with the number of replacements given to us
        longest_window = 0
        left = 0
        my_map = defaultdict(int) # To record the characters and their count inside
        for right in range(len(s)):
            curr_char = s[right]
            my_map[curr_char] += 1
            # 1. we first check if our current window is valid or not
            # The way we check its validity is to check the total number of characters we have encountered so far, and subtract the longest_window so far to see if it has exceeded our allowable replacement limit
            most_freq_elem_count = 0
            for count in my_map.values(): # Runs at most 26 times no matter the size of N, counts as O(1)
                most_freq_elem_count = max(count, most_freq_elem_count)
            
            # print("Current window size is", (right - left + 1), "with the substring", s[left : right + 1])
            # print("my_map is also currently", my_map)
            # print("most frequent element count is", most_freq_elem_count)
            while (right - left + 1) - most_freq_elem_count > k:
                # If our current window is no longer valid, we need to remove characters from our hashmap
                char_to_remove = s[left]
                my_map[char_to_remove] -= 1
                most_freq_elem_count = 0 # reset the frequency count
                for count in my_map.values(): # Runs at most 26 times no matter the size of N, counts as O(1)
                    most_freq_elem_count = max(count, most_freq_elem_count) # Recompute the most frequent element again
                left += 1
            
            longest_window = max(longest_window, right - left + 1)
        return longest_window

        