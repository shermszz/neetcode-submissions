class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        # Whether we can interleave s1 and s2 together to form s3
        s1_len, s2_len = len(s1), len(s2)

        # Trivial base case
        if len(s3) != (s1_len + s2_len):
            return False

        """ 
        Strat:
        - maintain 2 pointers, one for each string. 
        - Maintain a pointer that keeps moving forward for string s3
        - We will iterate through s3, and for each letter, we will check either s1 or s2 and see whether there is a matching character or not. 
        - There is a case when both characters could match. 
        - Hence, we need to make decisions and backtrack if one decision fails us    
        """

        first, second = 0, 0
        memo = {}
        def dfs(first: int, second: int) -> bool:
            if (first, second) in memo:
                return memo[(first,  second)]
            
            if first == len(s1) and second == len(s2):
                # we have reached the end of both strings successfully.
                return True
            
            curr_char = s3[first + second]
            path1, path2 = False, False
            if first < len(s1) and s1[first] == curr_char:
                # If it matches with s1, we try running the path down s1
                path1 = dfs(first + 1, second)
            if second < len(s2) and s2[second] == curr_char:
                path2 = dfs(first, second + 1)
           
            memo[(first, second)] = path1 or path2
            return memo[(first, second)]
        return dfs(first, second)
        





