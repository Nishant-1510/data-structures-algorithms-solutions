# Problem: Distinct Subsequence
# Approach: Use 2D DP where dp[i][j] counts ways to form t[0..j) from s[0..i) by either matching the current character or skipping it.
# Time Complexity: O(n * m)
# Space Complexity: O(n * m)

class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        cache = {}

        def dfs(i, j):
            if j == len(t):
                return 1
            if i == len(s):
                return 0
            if (i, j) in cache:
                return cache[(i, j)]

            if s[i] == t[j]:
                cache[(i, j)] = dfs(i + 1, j + 1) + dfs(i + 1, j)
            else:
                cache[(i, j)] = dfs(i + 1, j)
            return cache[(i, j)]

        return dfs(0,0)