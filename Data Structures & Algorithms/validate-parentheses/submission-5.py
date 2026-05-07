class Solution:
    def isValid(self, s: str) -> bool:
        # Only available chars are (), {} and []
        # Keep pushing to the stack if it is the opening bracket. 
        # If we encounter a closing bracket, it must match then we pop, otherwise return false
        stack = []
        for b in s:
            if b == '(' or b == '{' or b == '[':
                stack.append(b)
            elif b == ')':
                if len(stack) == 0 or stack[-1] != '(':
                    return False
                stack.pop() # valid bracket, so we pop it
            elif b == '}':
                if len(stack) == 0 or stack[-1] != '{':
                    return False
                stack.pop() # valid bracket, so we pop it
            elif b == ']':
                if len(stack) == 0 or stack[-1] != '[':
                    return False
                stack.pop() # valid bracket, so we pop it
        return len(stack) == 0
