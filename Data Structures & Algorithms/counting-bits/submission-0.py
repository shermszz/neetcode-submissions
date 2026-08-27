class Solution:
    def countBits(self, n: int) -> List[int]:
        num_ones = [0]
        for i in range(1, n + 1):
            # print("considering number", i)
            count = 0
            while i > 0:
                count += (i & 1)
                i = i >> 1
            num_ones.append(count)
        return num_ones