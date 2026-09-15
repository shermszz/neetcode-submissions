class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        """ 
            1. The first thing we need to check is that the length of hands is divisible by groupSize. If its not even divisible, then we can immediately return False.

            hand = [1, 2, 4, 2, 3, 5, 3, 4] --> length 8
            groupSize = 4
            2. Assuming divisible, then we need to ensure that each group has a strictly increasing number of values of value 1 only. 
            If i sort the array:
                hand = [1, 2, 2, 3, 3, 4, 5, 5], we know we have to split this into 2 groups.
            Now, we store each element and their frequency inside a hashmap. 
            We will loop through each number inside hand, and then we start with the smallest value in the array which is a 1. 
            We then check consecutively until we hit the groupSize number if there is a 1, 2, 3 and 4. 
                Everytime there is a value, we subtract the frequency count, removing the whole key if it has no more count left
            Once this first group is done, we take the next minimum value from a min heap 
        """
        hand_len = len(hand)
        if hand_len % groupSize != 0:
            return False
        my_map = Counter(hand) # This creates a frequency hashmap of every single value 
        # print(my_map)
        min_heap = list(my_map.keys()) # create a min_heap with all the unique values only
        heapq.heapify(min_heap)
        # print(min_heap)
        while min_heap: # While there are still values in the min_heap
            k = groupSize
            curr_num = min_heap[0]
            while k > 0:
                if curr_num not in my_map:
                    return False
                my_map[curr_num] -= 1
                if my_map[curr_num] == 0:
                    if curr_num != min_heap[0]: # The value that we pop must be the minimum, otherwise if we pop something larger with a number smaller than it, that smaller number later on will not be able to form a group, hence we can immediately return False here
                        return False
                    heapq.heappop(min_heap)
                curr_num += 1
                k -= 1 
        return True



        








