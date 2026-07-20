class Solution:
    def isValid(self, s: str) -> bool:
        brackets = {
            ")": "(",
            "}": "{",
            "]": "["
        }

        stack = []

        for i in range(len(s)):
            if s[i] not in brackets:
                stack.append(s[i])
            else:
                if not stack or stack[-1] != brackets[s[i]]:
                    return False
                stack.pop()

        return not stack

