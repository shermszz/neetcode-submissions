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
        print("t characters include", t_chars)

        def contained_within(current_window, t_chars):
            # Checking if t_chars is a subset of current_window, if yes then return true, otherwise false
            print("checking current window", current_window)
            # For each element in t_chars, check if it exists in current_window, and if the value / count is the same
            # The moment it doesnt exist, return false immediately
            # only return true if the loop completes
            for char, count in t_chars.items():
                if char not in current_window:
                    return False
                if current_window[char] < count:
                    return False
            
            return True
        
        # The shortest possible answer is a size of len(t) if it exists
        # Hence, we start with a window size of size len(t)
        left, right = 0, len(t)
        init_substring = s[left : right]
        curr_map = defaultdict(int)
        for i in init_substring:
            curr_map[i] += 1
        
        print("current window of characters is", curr_map)
        contains_substring = contained_within(curr_map, t_chars)
        print("Initial value", contains_substring)
        # Check here if curr_map is contained within t_chars

        shortest_string_so_far = init_substring if contains_substring else None 
        
        # Now, as we loop through the string s, we want to find a substring that contains the letters of t
        print("Length of string s", len(s))
        while right < len(s):
            # Keep adding characters into the map first
            char_to_add = s[right]
            curr_map[char_to_add] += 1
            right += 1

            # Now, we check again, whether curr_map is contained within t_chars
            contains_substring = contained_within(curr_map, t_chars)
            if contains_substring:
                curr_valid_substring = s[left : right]
                print("current valid substring is", curr_valid_substring)
                if shortest_string_so_far is None:
                    # First assignment
                    shortest_string_so_far = curr_valid_substring
                else:
                    shortest_string_so_far = curr_valid_substring if len(curr_valid_substring) < len(shortest_string_so_far) else shortest_string_so_far
                
                print("shortest string so far is", shortest_string_so_far)
                
                # Now, we try shrinking this current valid substring to see if we can still save its value
                while contains_substring:
                    # 1. First, we check if the current string is shorter than the shortest so far
                    if len(s[left : right]) < len(shortest_string_so_far):
                        shortest_string_so_far = s[left : right]
                    
                    # 2. Next, we try to shorten the string 
                    char_to_remove = s[left]
                    curr_map[char_to_remove] -= 1
                    if curr_map[char_to_remove] == 0:
                        del curr_map[char_to_remove]
                    left += 1
                    contains_substring = contained_within(curr_map, t_chars)
                    
        if shortest_string_so_far is None:
            return ""
        return shortest_string_so_far


