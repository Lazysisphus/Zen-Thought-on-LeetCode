class Solution:
    def isValid(self, s: str) -> bool:
        if not s:
            return True
        
        s = list(s)
        n = len(s)
        stack = [s[0]]
        for i in range(1, n):
            if s[i] in [")", "]", "}"] and not stack:
                return False
            elif s[i] == "]" and stack[-1] == "[":
                stack.pop()
            elif s[i] == "}" and stack[-1] == "{":
                stack.pop()
            elif s[i] == ")" and stack[-1] == "(":
                stack.pop()
            else:
                stack.append(s[i])
        if stack:
            return False
        else:
            return True