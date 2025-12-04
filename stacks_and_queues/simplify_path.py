# Problem: Simplify Path
# Approach: Normalize the path by using a stack to handle ".", ".." and valid directory names.
# Time Complexity:O(n)
# Space Complexity: O(n)
class Solution:
    def simplifyPath(self, path: str) -> str:
        stack = []
        cur = ""

        for c in path + "/":
            if c == "/":
                if cur == "..":
                    if stack: stack.pop()
                elif cur != "" and cur != ".":
                    stack.append(cur)
                cur = ""        

            else:
                cur += c  

        return "/" + "/".join(stack)          