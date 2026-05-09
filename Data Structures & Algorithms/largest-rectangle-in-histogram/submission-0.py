# Think of this question this way:
# If I use THIS bar as the roof of my rectangle,
# how far left or right can I stretch it before I hit a wall?
class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:        
        stack, largest = [], 0
        for curr_idx, curr_height in enumerate(heights):
            # Assume the bar starts at its own index by default
            start = curr_idx
            while stack and curr_height < stack[-1][1]:
                # The bar inside the stack has hit its bottleneck
                # Pop it, find its maximum area and update largest
                i, h = stack.pop()
                bottleneck_area = (curr_idx - i) * h
                largest = max(largest, bottleneck_area)
                
                # Crucially, we need to inherit the space BACKWARDS since the bar can actually extend backwards to a bar that is TALLER than itself
                start = i # This current shorter bar can stretch backwards into the popped bar's space
            
            # Otherwise, if the stack is empty OR the curr_height >= at the top of stack
            # We should just add it into the stack since the lower bar can stretch further
            stack.append((start, curr_height)) # Store as a tuple (index, height of bar)
        
        # If the stack still has values inside, there is no more boundaries for each of them, hence we can use the length of the array as the right boundary
        for i, h in stack:
            bottleneck_area = (len(heights) - i) * h
            largest = max(largest, bottleneck_area)
        
        return largest