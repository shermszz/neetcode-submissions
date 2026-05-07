class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        result = [0] * len(temperatures)
        for idx, curr in enumerate(temperatures):
            while stack and curr > temperatures[stack[-1]]:
                waiting_idx = stack.pop()
                num_days = idx - waiting_idx
                result[waiting_idx] = num_days    
            stack.append(idx)                
        return result


