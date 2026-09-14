class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        """
            n gas stations (circular in nautre)
            costs[i] = how much gas we need to get from i to (i + 1) % length
            car begins at any point with 0 gas
            
            We need to find the starting position inside gas such that we can return to this position with non-zero amount of gas

           Firstly, for this loop to work, we would need the total amount of gas that we top up to be >= the amount of gas that we need to burn in the loop 
        """
        # 1. check the base case
        if sum(gas) < sum(cost):
            return -1
        
        # Once we are here, we are guaranteed to have ONE solution 
        # The key idea is that we now start from the beginning of the array, and we measure what is the difference between gas[i] and cost[i]
        # Because if gas[i] - cost[i] < 0, then we know for sure that if we started at position i, we will not be able to complete the loop
        # Since there is guarantee of a solution, there will be a point where the total > 0, so we jsut need to remember that position and start from there to be able to complete the loop for sure. 
        start_pos = 0
        total = 0
        for i in range(len(gas)):
            total += (gas[i] - cost[i])
            if total < 0:
                # We restart again, the next possible starting position would have to be after this current position i
                # Because at any point from where we started up to the position where the total went below 0, that means any starting position from 0 to i is invalid, so we can just simply do start_pos = i + 1 and try again
                total = 0
                start_pos = i + 1
        return start_pos


