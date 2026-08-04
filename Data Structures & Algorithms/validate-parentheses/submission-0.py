class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        brackets_map = { "(": ")", "{":"}", "[":"]"}

        for bracket in s:
            print(stack)
            if bracket in brackets_map:
                stack.append(bracket)
            elif stack and brackets_map[stack[-1]] == bracket:
                stack.pop()
            else:
                return False

        return stack == []