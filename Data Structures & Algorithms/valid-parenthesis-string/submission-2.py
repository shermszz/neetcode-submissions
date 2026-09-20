class Solution:
    def checkValidString(self, s: str) -> bool:
        """
        Questions I would ask in interview:
            1. Since * is an empty string, would s = ***** be valid?  I assume yes

        Plan:
            This is similar to valid parenthesis question. 
            We can maintain a stack to store the open brackets and pop the closing brackets
            The tricky part now is the * character. It can be anything
            (()* --> True

            One idea:
            have a count for the *
            star_count tracks how many * we have encountered so far
            missing_open tracks the number of missing open braces that we need
            missing_close tracks how many missing closing braces we need to main validity
            
            for every character inside the string s:
                open braces push into stack
                closing braces pop from stack if not empty.
                    s = ()*)
                    If stack is empty, this signals we are missing open braces
                    in such cases, we add 1 to missing_open. 
                * we will keep track of it as a separate count in star_count

            At the end of iteration, we need to check the validity
            missing_close would be the the size of the stack currently
            missing_open would have been updated along the way
            we add these 2 variables together
            if this sum exceeds star_count, we return False, otherwise True

            CORRECT IDEA:
                maintain a min_open and max_open variable
                The whole point is that if we see open braces, both min and max increases
                If we see closing braces, both min and max will decrease in count
                If we see a wildcard, we will treat one like a closing, the other like an open. Hence in this case, min would go down and max would go up.
                To check for validity, since the placing of max_open is important, if max_open ever falls below 0, that means we have encountered more closing brackets than open brackets at that point, which is immediately invalid.
                We always reset min_open to 0 because we have a choice to set it as a closing bracket, but if that will make it invalid, we obviosuly wouldnt do it, so we just reset it to 0
                At the end, to check if the string really is valid, we need to check if the number of open brackets has 0 in the range, because that would imply it is balanced, so we just need to check min_open == 0

        """
        min_open, max_open = 0, 0
        for c in s:
            if c == '(':
                min_open += 1
                max_open += 1
            elif c == ')':
                min_open -= 1
                max_open -= 1
            else:
                # This is a wildcard
                min_open -= 1 
                max_open += 1
            if max_open < 0:
                return False
            if min_open < 0:
                min_open = 0
        return min_open == 0