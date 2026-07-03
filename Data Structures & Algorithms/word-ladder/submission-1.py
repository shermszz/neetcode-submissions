class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        # To set up, we need to use BFS to find the shortest path from beginWord to endWord
        queue = deque()
        queue.append((beginWord, 1)) # The number is to track the step count
        set_wordList = set(wordList) 

        def generate_mutations(word: str) -> List[str]:
            mutations = []
            for i in range(len(word)):
                curr_char = word[i]
                for j in range(97, 123): # The 26 letters corresponding to 'a' --> 'z'
                    if curr_char == chr(j):
                        continue # Dont include the same letter
                    mutated_word = word[:i] + chr(j) + word[i + 1:]
                    mutations.append(mutated_word)
            return mutations

        while queue:
            curr_word, step_count = queue.popleft()
            print("Curr word is ", curr_word)
            if curr_word == endWord:
                return step_count
            
            # We need to find all the possible 1 letter differences between curr_word and all words in the wordList
            # However, wordList can be very long
            # Instead of comparing curr_word with every word in wordList, which would be up to 5000 * len(word) operations,
            # what we can do instead is to generate all possible mutations of curr_word, which is maximally 25 * len(word).
            # For each generated mutation, if it is in wordList, add it to the queue with an increased step_count. 
            # Hence, we needed to ensure wordList is a set and not a list for O(1) lookup
            mutations = generate_mutations(curr_word)
            for word in mutations:
                if word in set_wordList:
                    print("word added is", word)
                    set_wordList.remove(word) # To mark the word as visited!
                    queue.append((word, step_count + 1))
        return 0

"""
=========================================================
KEY LEARNINGS: Word Ladder (LeetCode 127)
=========================================================

CORE CONCEPTS:
1. Unweighted Shortest Path = BFS: Any time you need the "shortest 
   transformation/sequence" and steps cost the same amount, use a Queue. 
   Store the distance directly in the queue: `(node, distance)`.
2. Generative Mutation vs. Dictionary Scanning: When $N$ (dictionary 
   size) is massive, but the node itself is small (a 10-letter word), 
   DO NOT scan the dictionary to find neighbors. Generate the neighbors 
   yourself ($O(26 \times M)$) and use an $O(1)$ Hash Set to check if 
   they exist.
3. The Set Removal Visited Trick: If you convert the given list/array 
   into a `set()`, you don't need a separate `visited` array. Just 
   `set.remove(word)` the moment you add it to the queue.

GUIDING HINTS & TRAPS AVOIDED:
- String Immutability: In Python, you cannot do `word[i] = 'a'`. You 
  MUST use string slicing: `word[:i] + new_char + word[i+1:]`. 
  Remember that slicing takes $O(M)$ time!
=========================================================
"""