class Solution {
    public int hammingWeight(int n) {
        int numOnes = 0;
        int result = n;
        while (result > 0) { // Will iterate maximally 32 times, since n = 32 bit integer
            numOnes += (result & 1); //Take the current n AND 1 to check if it is a 1
            result = result >>> 1; // SHIFT RIGHT LOGICAL by 1 bit to get rid of the value we just checked
        }
        return numOnes;

    }
}
