class Solution:
    def isValid(self, s: str) -> bool:
        if not s:
            return True

        ref = {"{": "}", "[": "]", "(": ")"}
        stack = []
        for i in range(len(s)):
            if (s[i] == "{"
                or s[i] == "["
                or s[i] == "("):
                stack.append(s[i])
            if (s[i] == "}"
                or s[i] == "]"
                or s[i] == ")"):
                if not stack:
                    return False
                else:
                    key = stack.pop()
                    if ref[key] != s[i]:
                        return False
        if not stack:
            return True
        else:
            return False