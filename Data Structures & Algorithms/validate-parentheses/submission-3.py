class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        look_up = {
            "{": "}",
            "(":")",
            "[":"]"
        }
        for i in s:
            if i in look_up:
                stack.append(i)
            else:
                if len(stack) == 0:
                    return False
                elif i == look_up[stack[-1]]:
                    stack.pop()
                else:
                    return False
        if len(stack) == 0:
            return True
        else:
            return False
