class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        """ 
            GOAL: Return the longest substring that has no repeating characters.

            Idea:
                - We will iterate through the string from left to right
                - We can maintain a 'hashset' of the characters that we have seen so far
                - As we iterate, if we have not seen this character before, we will extend our right window pointer and add this character to our hashset.
                - Once we see a duplicate character, we need to shrink the window by shifting the left pointer inward and removing the character at that point from the hashmap until the current character at the right pointer is distinct. 

                - At every step, we need to record what the longest substring length we have seen so far is

            e.g. s = "zzxyabz"
        """

        longest = 0 
        characters = set()

        left, right = 0, 0 # To measure the length of the window
        while right < len(s):
            if s[right] not in characters:
                # simply add it into the hashset, and then move the right pointer forward
                characters.add(s[right])
                right += 1
            else:
                # In the set, so we need to continously remove the characters from the left
                while s[right] in characters:
                    to_remove = s[left]
                    characters.remove(to_remove)
                    left += 1
            # Before moving on, record what is the longest substring you have seen so far
            longest = max(longest, right - left)
        return longest


