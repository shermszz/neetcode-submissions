class Solution:
    def isPalindrome(self, s: str) -> bool:
        i, j = 0, len(s) - 1
        while i < j:
            left, right = s[i].lower(), s[j].lower()
            if not left.isalnum():
                i += 1
            elif not right.isalnum():
                j -= 1
            else:
                if left != right: # Not a palindrome anymore
                    # print("left character is", left, "and right character is", right)
                    return False
                i += 1
                j -= 1
        # If exit while loop successfully, return True
        return True