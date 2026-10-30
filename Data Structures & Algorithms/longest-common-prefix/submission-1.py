class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        """
            Idea: We need to complete this in linear time 
            - The first word is always the longest common prefix 
            - We will compare every other word. If we find a matching character, then we go to the next and check until we find a non matching character, at which point that is the end of the longest common prefix. 
        """
        if not strs:
            return ""
        
        longest = strs[0] # The longest common prefix is the first string
        for i in range(1, len(strs)):
            curr = strs[i]

            # Check char by char for any matching prefixes, break early for any mismatches
            bound = min(len(curr), len(longest))
            ending = bound
            for j in range(bound):
                if longest[j] != curr[j]:
                    ending = j # The last point in which they have matching prefixes
                    break

            if ending < 0:
                longest = ""
            else:
                longest = longest[:ending]
        return longest
                