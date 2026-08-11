class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        close = {"]": "[", "}": "{", ")": "("}

        for c in s:
            if c in "])}" and stack and stack[-1] != close[c]:
                return False
            elif c in "])}" and stack and stack[-1] == close[c]:
                stack.pop()

            else:
                stack.append(c)
            
        return True if not stack else False






