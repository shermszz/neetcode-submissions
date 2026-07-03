class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        # Need to build a graph first, where aech word in the wordlist must connect from beginWord to endWord
        # The condition to connect is to check for exactly 1 character difference. 

        # A solution would be to start with beginWord.
            # For each word in wordList, if single_letter_diff(word, beginWord), then we create an edge to it
        # Run BFS since we need to find the shortest path
        def single_letter_diff(word1: str, word2: str) -> bool:
            """ Length of word1 and word2 are guranateed to be the same."""
            if word1 == "" or word2 == "":
                return False
            diff_count = 0
            for i in range(len(word1)):
                if word1[i] != word2[i]:
                    diff_count += 1
            return diff_count == 1
        
        adj_list = defaultdict(list)
        queue = deque()
        queue.append((beginWord, 1)) # 2nd number is the step count to reach endWord
        while queue:
            # Iterate through the wordList, to find the words that are 1 letter difference away
            curr_word, step_count = queue.popleft()
            if curr_word == endWord:
                return step_count
            
            for i in range(len(wordList)):
                if single_letter_diff(curr_word, wordList[i]):
                    queue.append((wordList[i], step_count + 1))
                    wordList[i] = "" # Mark this "word" as visited by changing it to the empty string
        return 0    
""" THIS IS NOT OPTIMAL """