# Problem: House Robber
# Approach: DP choosing max of robbing current + dp[i−2] or skipping to dp[i−1].
# Time Complexity: O(n)
# Space Complexity: O(1)
class Solution:
    def rob(self, nums: List[int]) -> int:
        rob1, rob2 = 0, 0

        # [rob1, rob2, n, n+1, ...]
        for n in nums:
            temp = max(n + rob1, rob2)
            rob1 = rob2
            rob2 = temp
        return rob2