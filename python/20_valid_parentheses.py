# regular stack
class Solution1:
    def isValid(self, s: str) -> bool:
        pairs = {"(": ")", "{": "}", "[": "]"}
        stack = []
        for i in s:
            if i in pairs:
                stack.append(i)
            elif stack and i == pairs[stack[-1]]:
                stack.pop()
            else:
                return False
        return stack == []


# hack
class Solution2:
    def isValid(self, s: str) -> bool:
        while "()" in s or "{}" in s or "[]" in s:
            s = s.replace("()", "")
            s = s.replace("{}", "")
            s = s.replace("[]", "")
        return s == ""


s = Solution2()
print(s.isValid("()"))  # true
print(s.isValid("()[]{}"))  # true
print(s.isValid("(]"))  # false
print(s.isValid("([)]"))  # false
print(s.isValid("{[]}"))  # true
