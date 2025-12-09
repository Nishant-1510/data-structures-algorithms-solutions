# Problem: Is Subsequence
# Approach: Use two pointers to match characters of s inside t in a single left-to-right scan.
# Time Complexity:O(n)
# Space Complexity: O(1)

class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        i, j = 0, 0

        while i < len(s) and j < len(t):
            if s[i] == t[j]:
                i += 1
            j += 1

        return True if i == len(s) else False   