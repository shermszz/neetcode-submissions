# This solution is the TOP-DOWN Dynamic Programming approach 
# Uses O(N) time and O(N) space
class Solution:
    def __init__(self):
        self.stairs = {}
    
    def climbStairs(self, n: int) -> int:
        # Check our cache to see if we already have the result.
        if n in self.stairs:
            return self.stairs[n] # the computed value
        if n == 1:
            self.stairs[n] = 1
            return 1
        if n == 2:
            self.stairs[n] = 2
            return 2
        # If not any of the base cases, we need to compute recursively, but updating the memoized table as we go
        self.stairs[n] = self.climbStairs(n - 1) + self.climbStairs(n - 2)
        return self.stairs[n]