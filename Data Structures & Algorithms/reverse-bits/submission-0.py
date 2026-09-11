class Solution:
    def reverseBits(self, n: int) -> int:
        res = 0 # To store the result of reversing all the bits 

        for i in range(32):
            # Extract the bit at the i-th position
            bit_val = (n >> i) & 1
            
            # We need to attach the bit_val to the (31 - i)th position inside result
            res |= (bit_val << (31 - i))
        return res