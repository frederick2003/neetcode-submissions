class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for token in tokens:
            if token == '+':
                stack.append(stack.pop() + stack.pop())
            elif token == '-':
                x = stack.pop()
                y = stack.pop()
                stack.append(y - x)
            elif token == '*':
                stack.append(stack.pop() * stack.pop())
            elif token == "/":
                x = stack.pop()
                y = stack.pop()
                stack.append(int(float(y) / float(x)))
            else:
                stack.append(int(token))
        return stack.pop()
                
