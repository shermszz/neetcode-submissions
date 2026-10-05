class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        # First we need to check whether we even have enough total gas  
        if sum(gas) < sum(cost):
            return -1
        
        # Assuming we have enough gas, we start at one position first
        start_pos = 0
        fuel = 0 # Start with 0 fuel
        for i in range(len(gas)):
            fuel += gas[i] # Top up at gas[i]
            fuel -= cost[i] # spend cost[i] to reach the new place
            if fuel < 0:
                # We do not have enough fuel to start at position i
                start_pos = i + 1
                fuel = 0
        return start_pos


        