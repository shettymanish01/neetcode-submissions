class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for ch in tokens:
            if ch == "+":
                a,b = stack.pop(), stack.pop()
                stack.append(a+b)
            elif ch == "-":
                a,b = stack.pop(), stack.pop()
                stack.append(b - a)
            elif ch == "*":
                a,b = stack.pop(), stack.pop()
                stack.append(a*b)
            elif ch == "/":
                a,b = stack.pop(), stack.pop()
                stack.append(int(float(b)/a))
            else:
                stack.append(int(ch))

        return stack[0]
            
