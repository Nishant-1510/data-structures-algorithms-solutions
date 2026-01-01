# Problem: Climbing Stairs
# Approach: Fibonacci-style DP where dp[i] = dp[i−1] + dp[i−2].
# Time Complexity: O(n)
# Space Complexity: O(n)

class Solution:
    def climbStairs(self, n: int) -> int:
        one, two = 1, 1

        for i in range(n - 1):
            temp = one
            one = one + two
            two = temp
            
        return one