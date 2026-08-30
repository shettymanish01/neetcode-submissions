class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        stack = []
        res = []

        def generate_parentheses(open_count, close_count):
            if close_count == open_count == n:
                print(stack)
                res.append("".join(stack))
                return

            if open_count < n:
                stack.append("(")
                generate_parentheses(open_count+1, close_count)
                stack.pop()
            if close_count < open_count:
                print(stack)
                stack.append(")")
                generate_parentheses(open_count, close_count+1)
                stack.pop()

        generate_parentheses(0,0)
        return res
