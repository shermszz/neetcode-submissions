class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        operators = {'+', '-', '*', '/'} # Set containing the basic math operators
        stack = []
        for token in tokens:
            if token in operators:
                print("current stack before popping both operands is ", stack)
                second_op = int(stack.pop())
                print(f"second op is {second_op}")
                first_op = int(stack.pop())
                print(f"first op is {first_op}")
                res = 0 # place holder value
                if token == '+':
                    res = first_op + second_op
                elif token == '-':
                    res = first_op - second_op
                elif token == '*':
                    res = first_op * second_op
                else:
                    res = int(first_op / second_op) # int() will truncate everything after the decimal point in floating point division
                print("final result after the operation is", res, "\n")
                stack.append(res)
            else:
                stack.append(token) # It must be some number
        # At the end should only have one value in stack
        return int(stack.pop())
