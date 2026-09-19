class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        """ 
            We need to find the shortest substring that would contain all the letters we encounter as we go along
            We will start at the front of the string and move forward.
            For example, s = xyxxyzbzbbisl
            we start at x, and we need to continue until the last x. (maybe use a hash map to store letter : last index of that letter during an initial pass)
            But there may be other letters inside that will extend the string. When we encounter those strings, we update the latest index to that letter if it exceeds the current latest index

        """

        # 1. Create a hashmap to store the letters and their latest index occurences
        my_map = {}
        for idx, letter in enumerate(s):
            my_map[letter] = idx # This will always update to the latest index

        # print(my_map)
        res = []  # To store the length of each substring

        # 2. Now, we start to iterate through the string with 2 pointers. 
        # one pointer (start) will keep moving, and everytime we encounter a new letter, the (end) pointer will shift to the point where we need to stop
        initial_starting = 0 # To keep track of the actual starting point of every substring
        start = 0
        end = -1
        while start < len(s):
            curr_letter = s[start]
            end = max(end, my_map[curr_letter])
            if start == end:
                # This is where we can return the length of the substring
                res.append(end - initial_starting + 1)
                initial_starting = start + 1
            start += 1
        return res

        
