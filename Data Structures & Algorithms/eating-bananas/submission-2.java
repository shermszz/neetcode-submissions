class Solution {
    public int minEatingSpeed(int[] piles, int h) {
        // h must be >= piles.length, otherwise it would be impossible to finish eating all the bananas
        // The least amount of bananas to eat per hour is 1
        // The max amount to eat is going to be the max(piles)
        int left = 1;
        int right = -1;
        for (int p : piles) right = Math.max(right, p); // Grab the maximum value 
        // System.out.println("Right bound is " + right);
        int k = Integer.MAX_VALUE;
        // Now, we perform a binary search to find the minimum k value if possible
        while (left <= right) {
            int mid_rate = left + (right - left) / 2;
            // System.out.println("Mid rate is " + mid_rate);
            long time_required = 0;
            for (int i = 0; i < piles.length; i++) {
                int bananas_left = Math.ceilDiv(piles[i], mid_rate);
                // ceilDiv replaces (a + b - 1) / b
                // System.out.println("Number of hours required to eat " + piles[i] + " bananas is " + bananas_left);
                time_required += bananas_left;
            }
            // System.out.println("Time required with " + mid_rate + " bananas per hour is " + time_required);
            if (time_required > h) {
                //Koko is eating too slow, need to be faster
                left = mid_rate + 1;
                // System.out.println("Shifting new lower bound eating rate to be " + left);
            } else {
                k = Math.min(mid_rate, k);
                //However, lets try to see if koko can eat fewer bananas
                right = mid_rate - 1;
                // System.out.println("Shifting upper bound to be lower at " + right + " bananas per hour");
            }
        }
        return k;
    }
}

/* 
=========================================================
KEY LEARNINGS: Koko Eating Bananas (LeetCode 875)
=========================================================

CORE CONCEPTS:
1. Binary Search on Answer: When a problem asks for the "minimum/maximum 
   value to satisfy a condition", and the condition is monotonic (eating 
   faster ALWAYS takes less time, eating slower ALWAYS takes more time), 
   it is a massive hint to Binary Search the answer range.
2. The Boundaries: The minimum possible speed is always 1. The maximum 
   useful speed is `max(piles)` because eating any faster than the biggest 
   pile still takes exactly 1 hour for that pile. Finding the max takes 
   $O(N)$, which is perfectly fine since our binary search does $O(N)$ work anyway.
3. The Ceiling Division Math Trick: To calculate ceiling division without 
   floating-point inaccuracies (like `Math.ceil((double) a / b)`), use 
   the integer math trick: `(a + b - 1) / b`. (Or `Math.ceilDiv(a, b)` in Java 18+).

INTERVIEW LEVEL-UP (The Accumulator Overflow):
- Whenever you are summing up values inside an array to check against a 
  limit (like accumulating total hours), ALWAYS declare your accumulator 
  as a `long` (`long time_required = 0;`). 
- Test cases are designed to intentionally push this sum past `Integer.MAX_VALUE`. 
  Spotting this before the interviewer points it out proves you write 
  production-safe code!
=========================================================
*/