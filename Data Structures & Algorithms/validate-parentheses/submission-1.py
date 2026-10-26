class Solution:
    def isValid(self, s: str) -> bool:
        mapper = {
            "}": "{",
            "]": "[",
            ")": "("
        }
        stack = []
        for i in s:
            if i in mapper:
                if len(stack) == 0:
                    return False
                elif stack[-1] == mapper[i]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(i)
        return True if len(stack) == 0 else False
