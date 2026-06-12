class Twitter:

    def __init__(self):
        self.tweets = defaultdict(list) # Hashmap of userIds --> list of tweets for this user

        # Need to keep track of who you follow to see their content
        self.followers = defaultdict(set) # hashmap of userIds -> set of followees
        self.time = 0 # Global time counter to track who posted at what time

    def postTweet(self, userId: int, tweetId: int) -> None:
        # post a tweet into the tweets dictionary with a timestamp
        self.tweets[userId].append((self.time, tweetId))
        self.time -= 1

    def getNewsFeed(self, userId: int) -> List[int]:
        # A user must also see his own feed
        self.followers[userId].add(userId)

        most_recent_tweets = [] # Max 10 tweet Ids
        all_tweets = [] # This will act as a min heap of k sorted lists
        for followeeId in self.followers[userId]:
            if self.tweets[followeeId]:
                index = len(self.tweets[followeeId]) - 1 # The end of the list has the most recent tweet
                time, tweetId = self.tweets[followeeId][index]
                heapq.heappush(all_tweets, (time, tweetId, followeeId, index))
      
        while all_tweets and len(most_recent_tweets) < 10:
            time, tweetId, followeeId, index = heapq.heappop(all_tweets)
            most_recent_tweets.append(tweetId)
            # We need to append back the next most recent tweet posted by followeeId at index -1
            if index > 0:
                new_time, new_tweetId = self.tweets[followeeId][index - 1]
                heapq.heappush(all_tweets, (new_time, new_tweetId, followeeId, index - 1))
            
        return most_recent_tweets

    def follow(self, followerId: int, followeeId: int) -> None:
        self.followers[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        self.followers[followerId].discard(followeeId) 
        # discard() Removes the item if it exists, otherwise do nothing

"""
=========================================================
KEY LEARNINGS: Design Twitter (LeetCode 355)
=========================================================

CORE CONCEPTS:
1. Object-Oriented Data Structures: 
   - Use `defaultdict(set)` for the Social Graph (`userId -> followees`).
   - Use `defaultdict(list)` for the Database (`userId -> tweets`).
2. Global Time: Simulating chronological order in a system requires a 
   global `time` counter that ticks every time an event occurs.
3. Merge K Sorted Lists (The Secret): Getting the top 10 recent 
   tweets from 500 users is just merging 500 sorted lists. You only 
   need to keep ONE item per list in the Heap at a time!

GUIDING HINTS:
- Fake Max-Heap: Start `time = 0` and decrement (`time -= 1`) on each 
  tweet. Smaller negative numbers bubble to the top of Python's Min-Heap.
- Self-Love: Always force the user to "follow" themselves in the 
  `getNewsFeed` function so their own tweets show up.
- The 4-Tuple Pointer: `(time, tweetId, followeeId, index)`.
  When you pop a tweet, look at its `index`. Go to that user's array, 
  grab the tweet at `index - 1`, and push it into the heap to replace it.
- Safe Removes: Use `set.discard()` instead of `set.remove()` to prevent 
  crashing if a user tries to unfollow someone they don't follow.
=========================================================
"""