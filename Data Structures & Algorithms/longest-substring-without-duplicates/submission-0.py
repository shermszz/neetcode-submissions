class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # Set a maxSoFar counter, and hashset to keep track of characters seen before
        prev = 0
        myChars = set() # To hold all ASCII characters
        maxSoFar = 0
        for curr in range(len(s)):
            while s[curr] in myChars:
                # Remove from the set
                myChars.remove(s[prev])
                prev += 1
            myChars.add(s[curr])
            maxSoFar = max(maxSoFar, curr - prev + 1)
        return maxSoFar


       