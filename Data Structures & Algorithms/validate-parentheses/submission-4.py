class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) % 2 != 0:
            return False

        ref = {"{": "}", "[": "]", "(": ")"}
        stack = []
        for c in s:
            if (c == "{"
                or c == "["
                or c == "("):
                stack.append(c)
            if (c == "}"
                or c == "]"
                or c == ")"):
                if not stack:
                    return False
                key = stack.pop()
                if c != ref[key]:
                    return False
        if not stack:
            return True
        else:
            return False