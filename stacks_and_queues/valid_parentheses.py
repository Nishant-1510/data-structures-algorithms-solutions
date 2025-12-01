# Problem: Valid Parentheses
# Approach: Use a stack to push opening brackets and pop when matching closing ones appear.
# Time Complexity:O(n)
# Space Complexity: O(n)

class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        closeToOpen = { ")" : "(" , "]" : "[" , "}" : "{" }

        for c in s:
            if c in closeToOpen:
                if stack and stack[-1] == closeToOpen[c]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(c)

        return True if not stack else False                    