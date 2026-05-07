class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        n = len(s) # number of characters in the string
        left, max_freq = 0, 0
        max_len = 0 #Track the max size window
        myMap = defaultdict(int)
        for right in range(n):
            curr_char = s[right]
            myMap[curr_char] += 1
            max_freq = max(max_freq, myMap[curr_char]) # keep track of the highest frequency character

            #Check window size validity
            if right - left + 1 - max_freq > k:
                # Window is too big, shrink with left pointer
                myMap[s[left]] -= 1 #Remove from the map 
                left += 1

            max_len = max(max_len, right - left + 1)
        return max_len



