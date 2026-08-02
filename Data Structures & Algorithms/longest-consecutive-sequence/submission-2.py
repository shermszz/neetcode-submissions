class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums_set = set(nums)
        for num in nums:
            nums_set.add(num)
        
        # print(nums_set)
        longest = 0
        
        # The trick to this question is that we will pull each number, and then check if its previous number is inside.
        # If the previous number is inside, that means it is part of a longer sequence, and we skip it
        for num in nums_set: # Iterate thorugh the set, dont go through nums, could have lots of duplicates
            # print("current number is", num)
            prev = num - 1
            if prev in nums_set:
                # This means that it is part of a longer sequence, ignore it first
                continue
            # If prev not in the set, it could be that it is the start of the longest sequence. 
            curr = num
            length = 0
            while curr in nums_set:
                # print("found", curr, "in the set, adding to longest length")
                length += 1
                curr += 1
            longest = max(longest, length)
            # print("longest so far is", longest)

        return longest