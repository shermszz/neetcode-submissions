class MinStack:

    def __init__(self):
        self.stack = [] # The regular stack
        self.min_stack = [] # This stack is to keep track of the actual minimum element

    def push(self, val: int) -> None:
        self.stack.append(val)
        if not self.min_stack:
            self.min_stack.append(val)
        else:
            curr_smallest = self.min_stack[-1]
            if val < curr_smallest:
                self.min_stack.append(val)
            else:
                self.min_stack.append(curr_smallest)

    def pop(self) -> None:
        self.min_stack.pop()
        self.stack.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        # To getMin, we look at the min_stack instead of the actual stack
        return self.min_stack[-1]
