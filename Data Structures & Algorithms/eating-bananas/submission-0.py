class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        # k is upperbounded to be the max of all piles[i] for all i, need to find a minimum
        # Lower bound is to eat 1 banana every hour only
        n = len(piles)
        lower = 1
        upper = 0
        for p in piles:
            if p > upper:
                upper = p
        # Now upper will hold the maximum value and is guaranteed to finish within h hours
        k = upper
        while lower <= upper:
            mid = lower + ((upper - lower) // 2)
            # This mid value is the number of bananas eaten every hour
            # Now, we calculate the time taken at this rate
            time = 0
            for p in piles:
                time += math.ceil(p / mid)
            if time <= h:
                k = mid # Record the smallest possible rate of banana eating
                # Continue to see if there is something smaller
                upper = mid - 1
            else:
                # This rate is too slow, increase the lower limit
                lower = mid + 1
        return k