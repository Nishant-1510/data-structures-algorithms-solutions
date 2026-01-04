# Problem: Unique Paths
# Approach: Use 2D DP where each cell represents the number of ways to reach it from the top or left.
# Time Complexity: O(n * m)
# Space Complexity: O(n)
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        row = [1] * n

        for i in range(m - 1):
            newRow = [1] * n
            for j in range(n -2, -1, -1):
                newRow[j] = newRow[j + 1] + row[j]
            row = newRow
        return row[0] 