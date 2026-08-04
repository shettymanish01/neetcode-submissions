class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        # stack = []
        # for ch in tokens:
        #     if ch == "+":
        #         a,b = stack.pop(), stack.pop()
        #         stack.append(a+b)
        #     elif ch == "-":
        #         a,b = stack.pop(), stack.pop()
        #         stack.append(b - a)
        #     elif ch == "*":
        #         a,b = stack.pop(), stack.pop()
        #         stack.append(a*b)
        #     elif ch == "/":
        #         a,b = stack.pop(), stack.pop()
        #         stack.append(int(float(b)/a))
        #     else:
        #         stack.append(int(ch))

        # return stack[0]

        def dfs():
            token = tokens.pop()
            operators = set(('+', '-','*','/'))

            if token not in operators:
                return int(token)

            b = dfs()
            a = dfs()

            if token == "+":
                return a + b
            elif token == "-":
                return a - b
            elif token == "*":
                return a * b
            elif token == "/":
                return int(a / b)

        return dfs()

        