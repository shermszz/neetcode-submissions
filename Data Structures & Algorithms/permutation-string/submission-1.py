class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        # Checking if s1 is inside of s2, but s1 can be any permutation of it
        # The ordering here matters.
        if len(s1) > len(s2):
            return False 

        # First, we can put each letter of s1 into a set
        s1_chars = defaultdict(int)
        for c in s1:
            s1_chars[c] += 1
        print("dict of s1 characters is", s1_chars)

        # start with 2 pointers
        left, right = 0, len(s1)
        curr_map = defaultdict(int)
        init_str = s2[left : right]
        for c in init_str:
            curr_map[c] += 1
    
        print("Initial map is", curr_map)
        while right < len(s2):
            print("curr map is", curr_map)
            if curr_map == s1_chars:
                return True
            # Otherwise, we need to update the map
            curr_map[s2[left]] -= 1
            if curr_map[s2[left]] == 0:
                del curr_map[s2[left]]
            curr_map[s2[right]] += 1
            right += 1
            left += 1
        # Outside, we need to check one more time
        return curr_map == s1_chars

