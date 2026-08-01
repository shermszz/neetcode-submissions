class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(t) > len(s):
            # even the entire string s itself cannot satisfy the length of t
            return ""

        # This is a dynamic sliding window size problem
        # First, we put the letters to t into a dictionary
        t_chars = defaultdict(int)
        for c in t:
            t_chars[c] += 1
        # print("t characters include", t_chars)

        left, right = 0, 0
        best_left = -1
        min_length = float('inf')
        curr_map = defaultdict(int)

        need, have = len(t_chars), 0 # Number of unique characters we need to satisfy VS what we currently have
        while right < len(s):
            # 1. We expand the size of our window first
            curr = s[right]
            curr_map[curr] += 1
            if curr in t_chars and curr_map[curr] == t_chars[curr]:
                have += 1 # We found one match so far
            right += 1

            # 2. Check whether we have found a string that has met all the requirements we need
            # If yes, then we can start testing if we can shrink the string into a shorter valid version
            while have == need:
                # Now, we can actively try to shrink the substring we found by shifting the left index in
                if (right - left) < min_length:
                    best_left = left
                    min_length = right - left
                char_to_remove = s[left]
                curr_map[char_to_remove] -= 1
                if curr_map[char_to_remove] == 0:
                    del curr_map[char_to_remove]
                # check if the character we removed was inside t_chars and whether its count now dropped below the necessary
                if char_to_remove in t_chars and curr_map[char_to_remove] < t_chars[char_to_remove]:
                    have -= 1 # we lost a valid character
                left += 1
        return s[best_left : best_left + min_length] if min_length != float('inf') else ""            



